from PySide6.QtWidgets import QMainWindow

from ui.loginUi import Ui_login


class LoginView(QMainWindow):
	def __init__(self, parent: QMainWindow = None):
		super(LoginView, self).__init__(parent)
		self.loginWindow_ = Ui_login()
		self.loginWindow_.setupUi(self)
