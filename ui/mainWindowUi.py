# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QStatusBar, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1031, 678)
        self.preference = QAction(mainWindow)
        self.preference.setObjectName(u"preference")
        self.help = QAction(mainWindow)
        self.help.setObjectName(u"help")
        self.about = QAction(mainWindow)
        self.about.setObjectName(u"about")
        self.feedback = QAction(mainWindow)
        self.feedback.setObjectName(u"feedback")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mainSplitter = QSplitter(self.centralwidget)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setOrientation(Qt.Orientation.Vertical)
        self.upperSplitter = QSplitter(self.mainSplitter)
        self.upperSplitter.setObjectName(u"upperSplitter")
        self.upperSplitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget_2 = QWidget(self.upperSplitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.optionsLayout = QVBoxLayout(self.layoutWidget_2)
        self.optionsLayout.setObjectName(u"optionsLayout")
        self.optionsLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.majorRangeBox = QComboBox(self.layoutWidget_2)
        self.majorRangeBox.setObjectName(u"majorRangeBox")
        self.majorRangeBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.majorRangeBox)


        self.optionsLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.studentTypeBox = QComboBox(self.layoutWidget_2)
        self.studentTypeBox.setObjectName(u"studentTypeBox")
        self.studentTypeBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.studentTypeBox)


        self.optionsLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.campusBox = QComboBox(self.layoutWidget_2)
        self.campusBox.setObjectName(u"campusBox")
        self.campusBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.campusBox)


        self.optionsLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.collegeBox = QComboBox(self.layoutWidget_2)
        self.collegeBox.setObjectName(u"collegeBox")
        self.collegeBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.collegeBox)


        self.optionsLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.startWeekBox = QComboBox(self.layoutWidget_2)
        self.startWeekBox.setObjectName(u"startWeekBox")
        self.startWeekBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.startWeekBox)


        self.optionsLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.endWeekBox = QComboBox(self.layoutWidget_2)
        self.endWeekBox.setObjectName(u"endWeekBox")
        self.endWeekBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.endWeekBox)


        self.optionsLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.dayBox = QComboBox(self.layoutWidget_2)
        self.dayBox.setObjectName(u"dayBox")
        self.dayBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_7.addWidget(self.dayBox)


        self.optionsLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.layoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.courseNameEdit = QLineEdit(self.layoutWidget_2)
        self.courseNameEdit.setObjectName(u"courseNameEdit")
        self.courseNameEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_9.addWidget(self.courseNameEdit)


        self.optionsLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.teacherNameEdit = QLineEdit(self.layoutWidget_2)
        self.teacherNameEdit.setObjectName(u"teacherNameEdit")
        self.teacherNameEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.teacherNameEdit)


        self.optionsLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.queryBtn = QPushButton(self.layoutWidget_2)
        self.queryBtn.setObjectName(u"queryBtn")
        self.queryBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.queryBtn)

        self.resetBtn = QPushButton(self.layoutWidget_2)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.resetBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.optionsLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.optionsLayout.addItem(self.verticalSpacer_2)

        self.upperSplitter.addWidget(self.layoutWidget_2)
        self.serviceTabWidget = QTabWidget(self.upperSplitter)
        self.serviceTabWidget.setObjectName(u"serviceTabWidget")
        self.courseQuery = QWidget()
        self.courseQuery.setObjectName(u"courseQuery")
        self.gridLayout_2 = QGridLayout(self.courseQuery)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.courseQueryLayout = QVBoxLayout()
        self.courseQueryLayout.setObjectName(u"courseQueryLayout")
        self.label_3 = QLabel(self.courseQuery)
        self.label_3.setObjectName(u"label_3")

        self.courseQueryLayout.addWidget(self.label_3)

        self.courseTableView = QTableView(self.courseQuery)
        self.courseTableView.setObjectName(u"courseTableView")
        self.courseTableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.courseTableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.courseTableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.courseTableView.setSortingEnabled(True)
        self.courseTableView.setWordWrap(False)
        self.courseTableView.horizontalHeader().setMinimumSectionSize(0)
        self.courseTableView.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.courseTableView.horizontalHeader().setStretchLastSection(True)
        self.courseTableView.verticalHeader().setMinimumSectionSize(0)
        self.courseTableView.verticalHeader().setDefaultSectionSize(20)

        self.courseQueryLayout.addWidget(self.courseTableView)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.firstPageBtn = QPushButton(self.courseQuery)
        self.firstPageBtn.setObjectName(u"firstPageBtn")
        self.firstPageBtn.setEnabled(False)
        self.firstPageBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_11.addWidget(self.firstPageBtn)

        self.previousPageBtn = QPushButton(self.courseQuery)
        self.previousPageBtn.setObjectName(u"previousPageBtn")
        self.previousPageBtn.setEnabled(False)
        self.previousPageBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_11.addWidget(self.previousPageBtn)

        self.currentPageLabel = QLabel(self.courseQuery)
        self.currentPageLabel.setObjectName(u"currentPageLabel")

        self.horizontalLayout_11.addWidget(self.currentPageLabel)

        self.label_13 = QLabel(self.courseQuery)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.maxPageLabel = QLabel(self.courseQuery)
        self.maxPageLabel.setObjectName(u"maxPageLabel")

        self.horizontalLayout_11.addWidget(self.maxPageLabel)

        self.nextPageBtn = QPushButton(self.courseQuery)
        self.nextPageBtn.setObjectName(u"nextPageBtn")
        self.nextPageBtn.setEnabled(False)
        self.nextPageBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_11.addWidget(self.nextPageBtn)

        self.lastPageBtn = QPushButton(self.courseQuery)
        self.lastPageBtn.setObjectName(u"lastPageBtn")
        self.lastPageBtn.setEnabled(False)
        self.lastPageBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_11.addWidget(self.lastPageBtn)

        self.pageSpinBox = QSpinBox(self.courseQuery)
        self.pageSpinBox.setObjectName(u"pageSpinBox")
        self.pageSpinBox.setMinimum(1)
        self.pageSpinBox.setMaximum(1)

        self.horizontalLayout_11.addWidget(self.pageSpinBox)

        self.label_14 = QLabel(self.courseQuery)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_11.addWidget(self.label_14)

        self.jumpPageBtn = QPushButton(self.courseQuery)
        self.jumpPageBtn.setObjectName(u"jumpPageBtn")
        self.jumpPageBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_11.addWidget(self.jumpPageBtn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.courseQueryLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.operateCourseBtn = QPushButton(self.courseQuery)
        self.operateCourseBtn.setObjectName(u"operateCourseBtn")
        self.operateCourseBtn.setEnabled(False)
        self.operateCourseBtn.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_12.addWidget(self.operateCourseBtn)

        self.addAutoBtn = QPushButton(self.courseQuery)
        self.addAutoBtn.setObjectName(u"addAutoBtn")
        self.addAutoBtn.setEnabled(False)
        self.addAutoBtn.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_12.addWidget(self.addAutoBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)


        self.courseQueryLayout.addLayout(self.horizontalLayout_12)


        self.gridLayout_2.addLayout(self.courseQueryLayout, 0, 0, 1, 1)

        self.serviceTabWidget.addTab(self.courseQuery, "")
        self.autoSelector = QWidget()
        self.autoSelector.setObjectName(u"autoSelector")
        self.gridLayout = QGridLayout(self.autoSelector)
        self.gridLayout.setObjectName(u"gridLayout")
        self.autoSelectorLayout = QVBoxLayout()
        self.autoSelectorLayout.setObjectName(u"autoSelectorLayout")
        self.label_6 = QLabel(self.autoSelector)
        self.label_6.setObjectName(u"label_6")

        self.autoSelectorLayout.addWidget(self.label_6)

        self.autoCourseTableLayout = QHBoxLayout()
        self.autoCourseTableLayout.setObjectName(u"autoCourseTableLayout")
        self.autoCourseTableView = QTableView(self.autoSelector)
        self.autoCourseTableView.setObjectName(u"autoCourseTableView")
        self.autoCourseTableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.autoCourseTableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.autoCourseTableView.setWordWrap(False)
        self.autoCourseTableView.horizontalHeader().setMinimumSectionSize(0)
        self.autoCourseTableView.horizontalHeader().setStretchLastSection(True)
        self.autoCourseTableView.verticalHeader().setVisible(True)
        self.autoCourseTableView.verticalHeader().setMinimumSectionSize(0)
        self.autoCourseTableView.verticalHeader().setDefaultSectionSize(20)

        self.autoCourseTableLayout.addWidget(self.autoCourseTableView)

        self.autoButtonLayout = QVBoxLayout()
        self.autoButtonLayout.setObjectName(u"autoButtonLayout")
        self.delAutoBtn = QPushButton(self.autoSelector)
        self.delAutoBtn.setObjectName(u"delAutoBtn")
        self.delAutoBtn.setMinimumSize(QSize(110, 30))

        self.autoButtonLayout.addWidget(self.delAutoBtn)

        self.switchAutoBtn = QPushButton(self.autoSelector)
        self.switchAutoBtn.setObjectName(u"switchAutoBtn")
        self.switchAutoBtn.setMinimumSize(QSize(110, 30))

        self.autoButtonLayout.addWidget(self.switchAutoBtn)

        self.clearAutoBtn = QPushButton(self.autoSelector)
        self.clearAutoBtn.setObjectName(u"clearAutoBtn")
        self.clearAutoBtn.setMinimumSize(QSize(110, 30))

        self.autoButtonLayout.addWidget(self.clearAutoBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.autoButtonLayout.addItem(self.verticalSpacer)


        self.autoCourseTableLayout.addLayout(self.autoButtonLayout)


        self.autoSelectorLayout.addLayout(self.autoCourseTableLayout)


        self.gridLayout.addLayout(self.autoSelectorLayout, 0, 0, 1, 1)

        self.serviceTabWidget.addTab(self.autoSelector, "")
        self.upperSplitter.addWidget(self.serviceTabWidget)
        self.mainSplitter.addWidget(self.upperSplitter)
        self.layoutWidget = QWidget(self.mainSplitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.logLayout = QVBoxLayout(self.layoutWidget)
        self.logLayout.setObjectName(u"logLayout")
        self.logLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.logLayout.addWidget(self.label_5)

        self.logPlainEdit = QPlainTextEdit(self.layoutWidget)
        self.logPlainEdit.setObjectName(u"logPlainEdit")
        self.logPlainEdit.setReadOnly(True)
        self.logPlainEdit.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.logLayout.addWidget(self.logPlainEdit)

        self.mainSplitter.addWidget(self.layoutWidget)

        self.gridLayout_3.addWidget(self.mainSplitter, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1031, 33))
        font = QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.preference)
        self.menu_2.addAction(self.help)
        self.menu_2.addAction(self.about)
        self.menu_2.addAction(self.feedback)

        self.retranslateUi(mainWindow)

        self.serviceTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u9009\u8bfe\u52a9\u624b", None))
        self.preference.setText(QCoreApplication.translate("mainWindow", u"\u9996\u9009\u9879", None))
        self.help.setText(QCoreApplication.translate("mainWindow", u"\u4f7f\u7528\u5e2e\u52a9", None))
        self.about.setText(QCoreApplication.translate("mainWindow", u"\u5173\u4e8e\u8f6f\u4ef6", None))
        self.feedback.setText(QCoreApplication.translate("mainWindow", u"\u95ee\u9898\u53cd\u9988", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u8bfe\u7a0b\u8303\u56f4\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\u9002\u7528\u5b66\u751f\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u8bfe\u6240\u5728\u6821\u533a\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u8bfe\u9662\u7cfb\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u8bfe\u8d77\u59cb\u5468\u6b21\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u8bfe\u622a\u6b62\u5468\u6b21\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"\u4e0a\u8bfe\u65f6\u95f4\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"\u8bfe\u7a0b\u540d\u79f0\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"\u4efb\u8bfe\u6559\u5e08\uff1a", None))
        self.queryBtn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.resetBtn.setText(QCoreApplication.translate("mainWindow", u"\u91cd\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\u8bfe\u7a0b\u5217\u8868\uff1a", None))
        self.firstPageBtn.setText(QCoreApplication.translate("mainWindow", u"\u9996\u9875", None))
        self.previousPageBtn.setText(QCoreApplication.translate("mainWindow", u"\u4e0a\u4e00\u9875", None))
        self.currentPageLabel.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.label_13.setText(QCoreApplication.translate("mainWindow", u"/", None))
        self.maxPageLabel.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.nextPageBtn.setText(QCoreApplication.translate("mainWindow", u"\u4e0b\u4e00\u9875", None))
        self.lastPageBtn.setText(QCoreApplication.translate("mainWindow", u"\u5c3e\u9875", None))
        self.label_14.setText(QCoreApplication.translate("mainWindow", u"\u9875", None))
        self.jumpPageBtn.setText(QCoreApplication.translate("mainWindow", u"\u8df3\u8f6c", None))
        self.operateCourseBtn.setText(QCoreApplication.translate("mainWindow", u"\u9009\u62e9\u8bfe\u7a0b", None))
        self.addAutoBtn.setText(QCoreApplication.translate("mainWindow", u"\u52a0\u5165\u62a2\u8bfe", None))
        self.serviceTabWidget.setTabText(self.serviceTabWidget.indexOf(self.courseQuery), QCoreApplication.translate("mainWindow", u"\u9009\u8bfe\u4e2d\u5fc3", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"\u5faa\u73af\u62a2\u8bfe\u8bfe\u7a0b\u5217\u8868\uff1a", None))
        self.delAutoBtn.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664\u9009\u4e2d\u7684\u8bfe\u7a0b", None))
        self.switchAutoBtn.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u59cb\u5faa\u73af\u62a2\u8bfe", None))
        self.clearAutoBtn.setText(QCoreApplication.translate("mainWindow", u"\u6e05\u7a7a\u8bfe\u7a0b\u5217\u8868", None))
        self.serviceTabWidget.setTabText(self.serviceTabWidget.indexOf(self.autoSelector), QCoreApplication.translate("mainWindow", u"\u62a2\u8bfe\u4e2d\u5fc3", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"\u64cd\u4f5c\u65e5\u5fd7\uff1a", None))
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"\u8bbe\u7f6e", None))
        self.menu_2.setTitle(QCoreApplication.translate("mainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

