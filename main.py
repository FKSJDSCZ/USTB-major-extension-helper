import sys
import urllib3
import logging

from PySide6.QtWidgets import QApplication

from entity.NetworkAccessManager import NetworkAccessManager
from view.LoginView import LoginView
from view.MainWindowView import MainWindowView
from controller.LoginController import LoginController
from controller.MainWindowController import MainWindowController
from service.LoginService import LoginService

from service.MainWindowService import MainWindowService
from model.MainWindowModel import MainWindowModel

urllib3.disable_warnings()

logging.basicConfig(
	format='%(asctime)s - %(filename)s - %(funcName)s: %(lineno)s - %(levelname)s - %(message)s',
	level=logging.DEBUG
)

if __name__ == '__main__':
	manager = NetworkAccessManager(None)

	app = QApplication(sys.argv)

	loginView = LoginView()
	mainWindowView = MainWindowView()

	mainWindowModel = MainWindowModel()

	loginService = LoginService(manager)
	mainWindowService = MainWindowService(manager, mainWindowModel)

	loginController = LoginController(loginView, loginService)
	mainWindowController = MainWindowController(mainWindowView, mainWindowService, mainWindowModel)

	loginController.toMainWindow.connect(mainWindowController.viewInit)

	sys.exit(app.exec())
