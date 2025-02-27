from PySide6.QtCore import QObject, Signal

from view.LoginView import LoginView
from service.LoginService import LoginService


class LoginController(QObject):
	toMainWindow = Signal(str)

	def __init__(self, loginView: LoginView, loginService: LoginService):
		super().__init__()
		self.view_: LoginView = loginView
		self.service_: LoginService = loginService
		self._connectionInit()
		self.service_.getToken()
		self.view_.show()

	def _connectionInit(self):
		# from view
		self.view_.loginWindow_.refreshBtn.clicked.connect(self._onRefreshBtnClicked)

		# from service
		self.service_.qrCodeUpdated.connect(self._onQrCodeUpdated)
		self.service_.warningMsgUpdated.connect(self._onWarningMsgUpdated)
		self.service_.loginStatusUpdated.connect(self._onLoginStatusUpdated)

	def _onRefreshBtnClicked(self):
		self.view_.loginWindow_.warningLabel.clear()
		self.service_.getToken()

	def _onQrCodeUpdated(self):
		self.view_.loginWindow_.qrCodeLabel.setPixmap(self.service_.qrCodePixmap_.scaled(200, 200))

	def _onWarningMsgUpdated(self, warningMsg: str):
		self.view_.loginWindow_.warningLabel.setText(warningMsg)

	def _onLoginStatusUpdated(self):
		self.view_.close()
		self.toMainWindow.emit(self.service_.homePage_)
