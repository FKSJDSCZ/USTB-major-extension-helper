from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QCloseEvent
from ui.mainWindowUi import Ui_mainWindow


class MainWindowView(QMainWindow):
	def __init__(self, parent: QMainWindow = None):
		super(MainWindowView, self).__init__(parent)
		self.mainWindow_ = Ui_mainWindow()
		self.mainWindow_.setupUi(self)
		self.autoFileDialog_: QFileDialog = QFileDialog(self)

		self._exitMsgBoxInit()

	def _exitMsgBoxInit(self) -> None:
		self.exitMsgBox_: QMessageBox = QMessageBox(self)
		self.exitMsgBox_.setWindowTitle("退出应用")
		self.exitMsgBox_.setText("确认退出应用？")
		self.exitMsgBox_.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
		self.exitMsgBox_.button(QMessageBox.StandardButton.Yes).setText("退出")
		self.exitMsgBox_.button(QMessageBox.StandardButton.No).setText("取消")

	def closeEvent(self, event: QCloseEvent) -> None:
		self.exitMsgBox_.exec()
		event.ignore()
