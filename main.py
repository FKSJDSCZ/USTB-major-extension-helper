import logging
import sys
import urllib3

from PySide6.QtWidgets import QApplication

from entity.NetworkAccessManager import NetworkAccessManager
from view.LoginView import LoginView
from view.MainWindowView import MainWindowView
from controller.LoginController import LoginController
from controller.MainWindowController import MainWindowController
from service.LoginService import LoginService
from service.MainWindowService import MainWindowService
from model.MainWindowModel import MainWindowModel
from entity.GuiLogger import guiLogger

urllib3.disable_warnings()

if __name__ == '__main__':
	manager = NetworkAccessManager(None)

	app = QApplication(sys.argv)

	loginView = LoginView()
	mainWindowView = MainWindowView()

	guiLogger.config(
		guiWidget=mainWindowView.mainWindow_.logPlainEdit,
		logLevel=logging.DEBUG
	)

	mainWindowModel = MainWindowModel()

	loginService = LoginService(manager)
	mainWindowService = MainWindowService(manager, mainWindowModel)

	loginController = LoginController(loginView, loginService)
	mainWindowController = MainWindowController(mainWindowView, mainWindowService, mainWindowModel)

	loginController.toMainWindow.connect(mainWindowController.viewInit)

	sys.exit(app.exec())
