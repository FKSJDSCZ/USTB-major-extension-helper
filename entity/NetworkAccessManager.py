import json
import logging
from urllib.parse import urlencode

from PySide6.QtCore import QUrl, QByteArray, QObject
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply, QSsl, QSslSocket, QSslConfiguration


class NetworkAccessManager(QNetworkAccessManager):
	def __init__(self, parent: QObject = None):
		super().__init__(parent)
		self.setRedirectPolicy(QNetworkRequest.RedirectPolicy.ManualRedirectPolicy)

	def prepareRequest(self, url: str, params: dict) -> QNetworkRequest:
		paramStr = str()
		if params:
			paramStr = "?" + urlencode(params)
		req = QNetworkRequest(QUrl(url + paramStr))

		config = QSslConfiguration.defaultConfiguration()
		config.setProtocol(QSsl.SslProtocol.AnyProtocol)
		config.setPeerVerifyMode(QSslSocket.PeerVerifyMode.VerifyNone)
		req.setSslConfiguration(config)

		return req

	def get(
			self,
			url: str,
			callback: callable = None,
			params: dict = None,
			allow_redirects: bool = True,
			*other
	) -> QNetworkReply:
		reply = super().get(self.prepareRequest(url, params))
		# There is a bug. "reply" can be QStandardItem object occasionally.
		if not isinstance(reply, QNetworkReply):
			logging.critical(f"{type(reply)}, {reply.parent()}")
			return
		reply.finished.connect(lambda: self._handleRedirect(reply, callback, allow_redirects, 0, *other))
		return reply

	def post(
			self,
			url: str,
			callback: callable = None,
			params: dict[str, str] = None,
			payload: dict = None,
			content_type: str = "application/json",
			allow_redirects: bool = True,
			*other
	) -> QNetworkReply:
		req = self.prepareRequest(url, params)
		data = QByteArray()
		if content_type == "application/json":
			req.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
			if payload:
				data = QByteArray(json.dumps(payload).encode())
		elif content_type == "application/x-www-form-urlencoded":
			req.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/x-www-form-urlencoded")
			if payload:
				data = QByteArray(urlencode(payload).encode())

		reply = super().post(req, data)
		reply.finished.connect(lambda: self._handleRedirect(reply, callback, allow_redirects, 0, *other))
		return reply

	def _handleRedirect(
			self,
			reply: QNetworkReply,
			callback: callable,
			allow_redirects: bool,
			redirect_count: int,
			*other
	) -> None:
		if reply.error() != QNetworkReply.NetworkError.NoError:
			if callback:
				reply.finished.disconnect()
				reply.finished.connect(lambda: callback(reply, *other))
				reply.finished.emit()
			else:
				reply.deleteLater()
			return

		if allow_redirects and redirect_count < reply.request().maximumRedirectsAllowed():
			redirectUrl: QUrl = reply.header(QNetworkRequest.KnownHeaders.LocationHeader)
			if redirectUrl:
				reply.deleteLater()
				newReply = super().get(QNetworkRequest(redirectUrl))
				newReply.finished.connect(lambda: self._handleRedirect(newReply, callback, allow_redirects, redirect_count + 1, *other))
				logging.debug(f"Redirect to {redirectUrl.toString()}")
				return

		if callback:
			reply.finished.disconnect()
			reply.finished.connect(lambda: callback(reply, *other))
			reply.finished.emit()
		else:
			reply.deleteLater()
