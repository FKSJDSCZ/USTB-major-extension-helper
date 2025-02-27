# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(589, 361)
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_3.setFont(font1)
        self.label_3.setMouseTracking(True)

        self.verticalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.phoneNumberEdit = QLineEdit(self.centralwidget)
        self.phoneNumberEdit.setObjectName(u"phoneNumberEdit")
        self.phoneNumberEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.phoneNumberEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.smsCodeEdit = QLineEdit(self.centralwidget)
        self.smsCodeEdit.setObjectName(u"smsCodeEdit")
        self.smsCodeEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.smsCodeEdit)

        self.getmsgBtn = QPushButton(self.centralwidget)
        self.getmsgBtn.setObjectName(u"getmsgBtn")
        self.getmsgBtn.setEnabled(False)
        self.getmsgBtn.setMinimumSize(QSize(100, 30))
        self.getmsgBtn.setAutoDefault(False)
        self.getmsgBtn.setFlat(False)

        self.horizontalLayout.addWidget(self.getmsgBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.warningLabel = QLabel(self.centralwidget)
        self.warningLabel.setObjectName(u"warningLabel")
        self.warningLabel.setStyleSheet(u"QLabel { color : red; }")
        self.warningLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.warningLabel)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.setStretch(3, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(39, 27, 40, 27)
        self.qrCodeLabel = QLabel(self.centralwidget)
        self.qrCodeLabel.setObjectName(u"qrCodeLabel")
        self.qrCodeLabel.setMinimumSize(QSize(200, 200))

        self.verticalLayout_4.addWidget(self.qrCodeLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.loginBtn = QPushButton(self.centralwidget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setEnabled(False)
        self.loginBtn.setMinimumSize(QSize(0, 30))
        self.loginBtn.setAutoDefault(False)
        self.loginBtn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.loginBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.refreshBtn = QPushButton(self.centralwidget)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.refreshBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setOpenExternalLinks(True)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 7)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)

        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"\u7528\u6237\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("login", u"| \u7528\u6237\u767b\u5f55", None))
        self.label_3.setText(QCoreApplication.translate("login", u"\u6b22\u8fce\u767b\u5f55\u5317\u4eac\u79d1\u6280\u5927\u5b66\u4e13\u4e1a\u62d3\u5c55\u8bfe\u7a0b\u5e73\u53f0", None))
        self.phoneNumberEdit.setPlaceholderText(QCoreApplication.translate("login", u"\u8bf7\u8f93\u5165\u624b\u673a\u53f7", None))
        self.smsCodeEdit.setPlaceholderText(QCoreApplication.translate("login", u"\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801", None))
        self.getmsgBtn.setText(QCoreApplication.translate("login", u"\u83b7\u53d6\u9a8c\u8bc1\u7801", None))
        self.loginBtn.setText(QCoreApplication.translate("login", u"\u767b\u5f55", None))
        self.refreshBtn.setText(QCoreApplication.translate("login", u"\u5237\u65b0", None))
        self.label_2.setText(QCoreApplication.translate("login", u"<a href=\"https://mec.ustb.edu.cn\">\u4e13\u4e1a\u62d3\u5c55\u8bfe\u7a0b\u5e73\u53f0</a>", None))
    # retranslateUi

