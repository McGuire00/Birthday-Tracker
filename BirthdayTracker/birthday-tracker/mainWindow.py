# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main app progressdGVrJK.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFormLayout, QFrame,
                               QGridLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QScrollArea, QSizePolicy,
                               QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 579)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(900, 579))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setMaximumSize(QSize(16777215, 550))
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_pane = QFrame(self.main_body)
        self.left_pane.setObjectName(u"left_pane")
        self.left_pane.setMinimumSize(QSize(0, 0))
        self.left_pane.setMaximumSize(QSize(100, 16777215))
        self.left_pane.setStyleSheet(u"QFrame{\n"
                                     "	background-color: #000;\n"
                                     "}\n"
                                     "QPushButton{\n"
                                     "	padding: 20px 10px;\n"
                                     "	border: none;\n"
                                     "	border-radius: 10px;\n"
                                     "	background-color: #000;\n"
                                     "	color: #fff;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "	background-color:  rgb(0, 92, 157)\n"
                                     "}")
        self.left_pane.setFrameShape(QFrame.StyledPanel)
        self.left_pane.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_pane)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_pane_btn = QFrame(self.left_pane)
        self.left_pane_btn.setObjectName(u"left_pane_btn")
        self.left_pane_btn.setStyleSheet(u"")
        self.left_pane_btn.setFrameShape(QFrame.StyledPanel)
        self.left_pane_btn.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.left_pane_btn)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.home_btn_2 = QPushButton(self.left_pane_btn)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setStyleSheet(u"QPushButton{\n"
                                      "	background-image: url(./images/icons8-home-24.png);\n"
                                      "	background-position: left;\n"
                                      "	background-repeat: none;\n"
                                      "	padding-left: 20px;\n"
                                      "}\n"
                                      "\n"
                                      " ")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.home_btn_2)

        self.add_user_btn = QPushButton(self.left_pane_btn)
        self.add_user_btn.setObjectName(u"add_user_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_user_btn.sizePolicy().hasHeightForWidth())
        self.add_user_btn.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(13)
        self.add_user_btn.setFont(font)
        self.add_user_btn.setStyleSheet(u"QPushButton{\n"
                                        "	background-image: url(./images/icons8-customer-24.png);\n"
                                        "	background-position: left;\n"
                                        "	background-repeat: none;\n"
                                        "	padding-left: 20px;\n"
                                        "}")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.add_user_btn)


        self.verticalLayout_2.addWidget(self.left_pane_btn)

        self.setting_btn = QPushButton(self.left_pane)
        self.setting_btn.setObjectName(u"setting_btn")
        self.setting_btn.setStyleSheet(u"QPushButton{\n"
                                       "	background-image: url(./images/icons8-settings-20.png);\n"
                                       "	background-position: left;\n"
                                       "	background-repeat: none;\n"
                                       "	padding-left: 20px;\n"
                                       "}\n"
                                       "")

        self.verticalLayout_2.addWidget(self.setting_btn)


        self.horizontalLayout.addWidget(self.left_pane)

        self.main_pane = QFrame(self.main_body)
        self.main_pane.setObjectName(u"main_pane")
        self.main_pane.setMaximumSize(QSize(800, 16777215))
        self.main_pane.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.main_pane.setFrameShape(QFrame.StyledPanel)
        self.main_pane.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_pane)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.main_pane)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(900, 16777215))
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.home_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea = QScrollArea(self.home_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 748, 488))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.home_page)
        self.add_page = QWidget()
        self.add_page.setObjectName(u"add_page")
        self.add_page.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.verticalLayout_4 = QVBoxLayout(self.add_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.add_user_page = QFrame(self.add_page)
        self.add_user_page.setObjectName(u"add_user_page")
        self.add_user_page.setFrameShape(QFrame.StyledPanel)
        self.add_user_page.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.add_user_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.user_info_form = QFrame(self.add_user_page)
        self.user_info_form.setObjectName(u"user_info_form")
        self.user_info_form.setMinimumSize(QSize(0, 250))
        font1 = QFont()
        font1.setBold(True)
        self.user_info_form.setFont(font1)
        self.user_info_form.setStyleSheet(u"QPushButton:hover{\n"
                                          "	background-color:  rgb(0, 92, 157)\n"
                                          "}\n"
                                          "QLineEdit{\n"
                                          "	border: 2px solid rgb(45,45,45);\n"
                                          "	border-radius: 10px;\n"
                                          "	padding: 15px;\n"
                                          "	background-color: rgb(31,22,66);\n"
                                          "	color: rgb(255,255,255);\n"
                                          "	\n"
                                          "}\n"
                                          "QLineEdit:hover{\n"
                                          "	border: 2px solid rgb(0,66, 124);\n"
                                          "}\n"
                                          "QLineEdit:focus{\n"
                                          "	border: 2px solid rgb(206, 206, 206);\n"
                                          "	color: rgb(200, 200, 200);\n"
                                          "}")
        self.user_info_form.setFrameShape(QFrame.StyledPanel)
        self.user_info_form.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.user_info_form)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.first_name_label = QLabel(self.user_info_form)
        self.first_name_label.setObjectName(u"first_name_label")
        self.first_name_label.setEnabled(True)
        self.first_name_label.setMinimumSize(QSize(100, 40))
        self.first_name_label.setStyleSheet(u"border: 3px solid rgb(118, 231, 255);\n"
                                            "border-radius: 10px;\n"
                                            "color: rgb(0, 0, 0);")
        self.first_name_label.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.first_name_label)

        self.first_name_text = QLineEdit(self.user_info_form)
        self.first_name_text.setObjectName(u"first_name_text")
        self.first_name_text.setMinimumSize(QSize(200, 40))
        self.first_name_text.setStyleSheet(u"border: 3px solid rgb(118, 231, 255);\n"
                                           "border-radius: 10px;")
        self.first_name_text.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.first_name_text)

        self.last_name_label = QLabel(self.user_info_form)
        self.last_name_label.setObjectName(u"last_name_label")
        self.last_name_label.setMinimumSize(QSize(100, 40))
        self.last_name_label.setStyleSheet(u"border: 3px solid rgb(118, 231, 255);\n"
                                           "border-radius: 10px;\n"
                                           "color: rgb(0, 0, 0);")
        self.last_name_label.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.last_name_label)

        self.last_name_text = QLineEdit(self.user_info_form)
        self.last_name_text.setObjectName(u"last_name_text")
        self.last_name_text.setMinimumSize(QSize(200, 40))
        self.last_name_text.setStyleSheet(u"border: 3px solid rgb(118, 231, 255);\n"
                                          "border-radius: 10px;")
        self.last_name_text.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.last_name_text)

        self.birthday_label = QLabel(self.user_info_form)
        self.birthday_label.setObjectName(u"birthday_label")
        self.birthday_label.setMinimumSize(QSize(100, 40))
        self.birthday_label.setStyleSheet(u"border: 3px solid rgb(118, 231, 255);\n"
                                          "border-radius: 10px;\n"
                                          "color: rgb(0, 0, 0);")
        self.birthday_label.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.birthday_label)

        self.birthday_text = QLineEdit(self.user_info_form)
        self.birthday_text.setObjectName(u"birthday_text")
        self.birthday_text.setMinimumSize(QSize(200, 40))
        self.birthday_text.setStyleSheet(u"border: 3px solid rgb(118, 231, 255);\n"
                                         "border-radius: 10px;")
        self.birthday_text.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.birthday_text)

        self.submit_info_btn = QPushButton(self.user_info_form)
        self.submit_info_btn.setObjectName(u"submit_info_btn")
        self.submit_info_btn.setMinimumSize(QSize(200, 40))
        self.submit_info_btn.setStyleSheet(u"border: 3px solid rgb(118, 231, 255);\n"
                                           "border-radius: 10px;")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.submit_info_btn)


        self.gridLayout.addWidget(self.user_info_form, 1, 0, 1, 1)

        self.calendat_frame = QFrame(self.add_user_page)
        self.calendat_frame.setObjectName(u"calendat_frame")
        self.calendat_frame.setFrameShape(QFrame.StyledPanel)
        self.calendat_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.calendat_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.calendarWidget = QCalendarWidget(self.calendat_frame)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_7.addWidget(self.calendarWidget)


        self.gridLayout.addWidget(self.calendat_frame, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.add_user_page)

        self.stackedWidget.addWidget(self.add_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.verticalLayout_6 = QVBoxLayout(self.setting_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.setting_page)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.setting_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.main_pane)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMaximumSize(QSize(16777215, 30))
        self.main_footer.setStyleSheet(u"background-color: rgb(118, 214, 255);")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Birthday Tracker", None))
        self.home_btn_2.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.add_user_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.setting_btn.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.first_name_label.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.first_name_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.last_name_label.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.last_name_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.birthday_label.setText(QCoreApplication.translate("MainWindow", u"Birthday", None))
        self.birthday_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Birthday :", None))
        self.submit_info_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
    # retranslateUi

