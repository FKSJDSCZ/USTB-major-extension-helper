import logging
import sys
from logging.handlers import RotatingFileHandler
from PySide6.QtGui import QColor, QTextCharFormat, QTextCursor
from PySide6.QtWidgets import QPlainTextEdit, QApplication


class GuiLogger:
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self):
		self.logger_ = logging.getLogger("GuiLogger")
		self.handlers_ = {}
		self.colors_ = {
			'gui': {
				logging.DEBUG: QColor(100, 100, 100),
				logging.INFO: QColor(0, 0, 0),
				logging.WARNING: QColor(200, 100, 0),
				logging.ERROR: QColor(255, 0, 0),
				logging.CRITICAL: QColor(150, 0, 0)
			},
			'console': {
				logging.DEBUG: '\033[37m',  # 白色
				logging.INFO: '\033[36m',  # 青色
				logging.WARNING: '\033[33m',  # 黄色
				logging.ERROR: '\033[31m',  # 红色
				logging.CRITICAL: '\033[35m'  # 紫色
			}
		}
		self.defaultFormat_ = '[%(asctime)s] %(filename)s - %(funcName)s(Line %(lineno)s) - %(levelname)s: %(message)s'

	def config(
			self,
			enableGui: bool = True,
			enableConsole: bool = True,
			enableFile: bool = False,
			guiWidget: QPlainTextEdit = None,
			logLevel: int = logging.DEBUG,
			logFileName: str = 'mec.log',
			logFileMode: str = 'a',
			logFileMaxBytes: int = 1024 * 1024,
			logFileBackupCount: int = 10,
			logFormat: str = None,
			dateFormat: str = None
	):
		"""
		配置日志记录器
		:param enableGui: 启用GUI输出
		:param enableConsole: 启用控制台输出
		:param enableFile: 启用文件记录
		:param guiWidget: GUI输出组件
		:param logLevel: 日志等级
		:param logFileName: 日志文件路径
		:param logFileMode: 日志文件读写模式
		:param logFileMaxBytes: 单个日志文件最大大小（字节）
		:param logFileBackupCount: 备份文件数量
		:param logFormat: 日志格式
		:param dateFormat: 时间格式
		"""
		for handler in self.handlers_.values():
			self.logger_.removeHandler(handler)
		self.handlers_.clear()

		format_ = logging.Formatter(logFormat or self.defaultFormat_, datefmt=dateFormat)

		# GUI output
		if enableGui and guiWidget:
			guiHandler = GuiLogHandler(guiWidget)
			guiHandler.setFormatter(format_)
			guiHandler.setColors(self.colors_['gui'])
			self.handlers_['gui'] = guiHandler
			self.logger_.addHandler(guiHandler)

		# console output
		if enableConsole:
			consoleHandler = ConsoleLogHandler()
			consoleHandler.setFormatter(format_)
			consoleHandler.setColors(self.colors_['console'])
			self.handlers_['console'] = consoleHandler
			self.logger_.addHandler(consoleHandler)

		# file output
		if enableFile:
			fileHandler = RotatingFileHandler(
				logFileName,
				mode=logFileMode,
				maxBytes=logFileMaxBytes,
				backupCount=logFileBackupCount,
				encoding='utf-8'
			)
			fileHandler.setFormatter(format_)
			self.handlers_['file'] = fileHandler
			self.logger_.addHandler(fileHandler)

		self.logger_.setLevel(logLevel)
		for handler in self.handlers_.values():
			handler.setLevel(logLevel)

	def setGuiColors(self, colorDict: dict):
		if 'gui' in self.handlers_:
			self.handlers_['gui'].setColors(colorDict)

	def setConsoleColors(self, colorDict: dict):
		if 'console' in self.handlers_:
			self.handlers_['console'].setColors(colorDict)

	def __getattr__(self, name):
		return getattr(self.logger_, name)


class GuiLogHandler(logging.Handler):
	def __init__(self, widget: QPlainTextEdit):
		super().__init__()
		self.widget_ = widget
		self.formats_ = {}

	def setColors(self, colors: dict):
		for level, color in colors.items():
			format_ = QTextCharFormat()
			format_.setForeground(color)
			self.formats_[level] = format_

	def emit(self, record):
		msg = self.format(record)
		format_ = self.formats_.get(record.levelno, QTextCharFormat())
		self.widget_.appendPlainText(msg)
		cursor = self.widget_.textCursor()
		cursor.movePosition(QTextCursor.MoveOperation.End)
		cursor.movePosition(QTextCursor.MoveOperation.StartOfLine, QTextCursor.MoveMode.KeepAnchor)
		cursor.mergeCharFormat(format_)


class ConsoleLogHandler(logging.StreamHandler):
	RESET = '\033[0m'

	def __init__(self):
		super().__init__()
		self.colors = {}

	def setColors(self, colorDict: dict):
		self.colors = colorDict

	def emit(self, record):
		color = self.colors.get(record.levelno, self.RESET)
		msg = self.format(record)
		self.stream.write(f"{color}{msg}{self.RESET}\n")
		self.flush()


guiLogger = GuiLogger()
