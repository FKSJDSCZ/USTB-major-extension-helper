import json
import re

from lxml import etree
from urllib.parse import urlparse, parse_qs
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QPixmap
from PySide6.QtNetwork import QNetworkRequest, QNetworkReply

from entity.NetworkAccessManager import NetworkAccessManager
from entity.GuiLogger import guiLogger

sisAuthDomain = "https://sis.ustb.edu.cn"
rootDomain = "https://mec.ustb.edu.cn"


class LoginService(QObject):
	qrCodeUpdated = Signal()
	warningMsgUpdated = Signal(str)
	loginStatusUpdated = Signal()

	def __init__(self, manager: NetworkAccessManager):
		super().__init__()
		self.appId_: str = str()
		self.randomToken_: str = str()
		self.sessionId_: str = str()
		self.homePage_: str = str()
		self.qrCodePixmap_: QPixmap = QPixmap()
		self.lastQrStateQuery_: QNetworkReply = None
		self.manager_: NetworkAccessManager = manager

	def getToken(self) -> None:
		"""Step 0: get appId and random token"""
		if self.lastQrStateQuery_:
			self.lastQrStateQuery_.finished.disconnect()
			self.lastQrStateQuery_.abort()
			self.lastQrStateQuery_.deleteLater()
			self.lastQrStateQuery_ = None
		self.manager_.get(
			f"{rootDomain}/logon",
			self._getQrCodeLink
		)

	def _getQrCodeLink(self, reply: QNetworkReply) -> None:
		"""Step 1: set appId and random token, then get Qr code link"""
		loginHtml = etree.HTML(reply.readAll().data().decode())
		scripts = loginHtml.xpath("//script[@type='text/javascript']/text()")
		for script in scripts:
			if script:
				self.appId_ = re.findall(r"appid:\s*['\"](.*?)['\"]", script)[0]
				self.randomToken_ = re.findall(r"rand_token:\s*['\"](.*?)['\"]", script)[0]
				returnUrl = re.findall(r"return_url:\s*['\"](.*?)['\"]", script)[0]

				self.manager_.get(
					f"{sisAuthDomain}/connect/qrpage",
					self._getQrCodeData,
					{
						"appid": self.appId_,
						"return_url": returnUrl,
						"rand_token": self.randomToken_,
						"embed_flag": 1
					}
				)
				break
		reply.deleteLater()

	def _getQrCodeData(self, reply: QNetworkReply) -> None:
		"""step 2: parse Qr code link, then get Qr Code image data"""
		qrCodeHtml: etree._Element = etree.HTML(reply.readAll().data().decode(), etree.HTMLParser())
		qrCodeLink = sisAuthDomain + qrCodeHtml.xpath("//img[@id='qrimg']/@src")[0]
		qrCodeLinkParams = parse_qs(urlparse(qrCodeLink).query)
		self.sessionId_ = qrCodeLinkParams["sid"][0]

		self.manager_.get(
			qrCodeLink,
			self._queryQrState,
		)
		reply.deleteLater()

	def _queryQrState(self, reply: QNetworkReply) -> None:
		"""step 3: load Qr Code data, then query Qr code state"""
		self.qrCodePixmap_.loadFromData(reply.readAll())
		self.qrCodeUpdated.emit()
		guiLogger.info("Successfully get Qr Code image data")

		self._sendCheckStateRequest()
		reply.deleteLater()

	def _sendCheckStateRequest(self):
		self.lastQrStateQuery_ = self.manager_.get(
			f"{sisAuthDomain}/connect/state",
			self._qrAuthenticate,
			{
				"sid": self.sessionId_
			},
		)

	def _qrAuthenticate(self, reply: QNetworkReply) -> None:
		"""step 4: check Qr code state, then login"""
		if parse_qs(urlparse(reply.request().url().toString()).query)["sid"][0] == self.sessionId_:
			resData = json.loads(reply.readAll().data().decode())
			if resData["code"] == 1:
				self.warningMsgUpdated.emit("登录中...")
				self.manager_.get(
					f"{rootDomain}/sisLogin",
					self._login,
					{
						"appid": self.appId_,
						"auth_code": resData["data"],
						"rand_token": self.randomToken_,
					}
				)
			elif resData["code"] == 2:
				emitMsg = ("企业" if resData["data"] == "WxWork" else str()) + "微信已扫码，请确认"
				self.warningMsgUpdated.emit(emitMsg)
			elif resData["code"] == 3 or resData["code"] > 200:
				self.warningMsgUpdated.emit("二维码已失效，请刷新")
			elif resData["code"] == 4:
				self.warningMsgUpdated.emit(str())
			elif resData["code"] == 0:
				self.warningMsgUpdated.emit("请求状态异常")
			elif resData["code"] == 101:
				self.warningMsgUpdated.emit("请求的方法不被允许")
			elif resData["code"] == 102:
				self.warningMsgUpdated.emit("请求不合法")
			else:
				self.warningMsgUpdated.emit(f"[{resData['code']}]{resData['message']}")

			if resData["code"] in [2, 4]:
				self._sendCheckStateRequest()
			else:
				self.lastQrStateQuery_ = None

			guiLogger.info(f"QR code state info: [{resData['code']}] {resData['message']}")
		reply.deleteLater()

	def _login(self, reply: QNetworkReply) -> None:
		"""Step 5: login, then switch the view"""
		self.homePage_ = reply.readAll().data().decode()
		homePageHtml: etree._Element = etree.HTML(self.homePage_)
		errorContent = homePageHtml.xpath("//div[@class='error-content']")
		if errorContent:
			self.warningMsgUpdated.emit(errorContent[0].xpath(".//p/text()")[0])
			guiLogger.warning("Failed to login")
		else:
			self.loginStatusUpdated.emit()
			guiLogger.info("Successfully login")
		reply.deleteLater()
