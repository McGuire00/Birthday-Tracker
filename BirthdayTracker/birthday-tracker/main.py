from mainWindow import *
from database import *
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QVBoxLayout


class MAIN_APP(Ui_MainWindow):
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Gives the buttons functions
        self.ui.add_user_btn.clicked.connect(self.showAddUser)
        self.ui.home_btn_2.clicked.connect(self.showHome)
        self.ui.setting_btn.clicked.connect(self.showSettings)
        self.ui.submit_info_btn.clicked.connect(self.submitNewPerson)
        self.ui.calendarWidget.clicked.connect(self.update_birthday_field)

        dbupdate()
        self.updateHomePage()

        # Sets grid on calendar
        # self.ui.calendarWidget.setGridVisible(True)

    def updateHomePage(self):
        try:
            values = cursor.execute("Select * FROM Birthdays")
        except Exception as e:
            print(f"Error occured : {e}")
        length_of_db = values.fetchall()
        if length_of_db != 0:
            try:
                values = cursor.execute("SELECT * FROM Birthdays ORDER BY DaysUntilBirthday ASC")
                y = 3
                for row in values:
                    birthday = datetime.datetime.strptime(row[3], "%Y-%m-%d")
                    Day = birthday.day
                    formatted = "th"
                    if Day == 1 or Day == 21 or Day == 31:
                        formatted = "st"
                    if Day == 2 or Day == 22:
                        formatted = "nd"
                    if Day == 3 or Day == 23:
                        formatted = "rd"
                    birthday = birthday.strftime(f"%B {Day}{formatted}!")
                    day_until = int(row[5])

                    self.BirthdayFrame = QFrame(self.ui.scrollAreaWidgetContents)
                    self.BirthdayFrame.setFrameShape(QFrame.Box)
                    self.BirthdayFrame.setFrameShadow(QFrame.Plain)
                    self.BirthdayFrame.setMinimumSize(QSize(720, 71))
                    self.BirthdayFrame.setMaximumSize(QSize(720, 71))
                    self.BirthdayFrame.setLineWidth(3)
                    self.BirthdayFrame.setMidLineWidth(2)
                    self.BirthdayFrame.setObjectName("BirthdayFrame")
                    self.Cake_Picture = QLabel(self.BirthdayFrame)
                    self.Cake_Picture.setGeometry(QRect(10, 3, 91, 65))
                    self.Cake_Picture.setFrameShape(QFrame.NoFrame)
                    self.Cake_Picture.setText("")
                    self.Cake_Picture.setPixmap(QPixmap(".images/BirthdayCakeIcon.png"))
                    self.Cake_Picture.setScaledContents(True)
                    self.Cake_Picture.setObjectName("Cake_Picture")
                    self.First_and_Last_Name = QLabel(self.BirthdayFrame)
                    self.First_and_Last_Name.setGeometry(QRect(120, 4, 521, 31))
                    font = QFont()
                    font.setFamily("Bahnschrift SemiBold")
                    font.setPointSize(14)
                    font.setBold(False)
                    font.setItalic(False)
                    # font.setWeight(50)
                    self.First_and_Last_Name.setFont(font)
                    self.First_and_Last_Name.setFrameShape(QFrame.NoFrame)
                    self.First_and_Last_Name.setFrameShadow(QFrame.Plain)
                    self.First_and_Last_Name.setText(f"{row[1]} {row[2]}")
                    self.First_and_Last_Name.setAlignment(Qt.AlignCenter)
                    self.First_and_Last_Name.setObjectName("First_and_Last_Name")
                    self.Turns_Age_On_Date = QLabel(self.BirthdayFrame)
                    self.Turns_Age_On_Date.setGeometry(QRect(120, 37, 521, 31))
                    font = QFont()
                    font.setFamily("Bahnschrift SemiBold")
                    font.setPointSize(14)
                    font.setBold(False)
                    font.setItalic(False)
                    # font.setWeight(50)
                    self.Turns_Age_On_Date.setFont(font)
                    self.Turns_Age_On_Date.setFrameShape(QFrame.NoFrame)
                    self.Turns_Age_On_Date.setFrameShadow(QFrame.Plain)
                    self.Turns_Age_On_Date.setText(f"Turns {row[4] + 1} on {birthday} ")
                    self.Turns_Age_On_Date.setAlignment(Qt.AlignCenter)
                    self.Turns_Age_On_Date.setObjectName("Turns_Age_On_Date")
                    self.Number_of_Days = QLabel(self.BirthdayFrame)
                    self.Number_of_Days.setGeometry(QRect(840, 3, 61, 31))
                    font = QFont()
                    font.setFamily("Bahnschrift SemiBold")
                    font.setPointSize(14)
                    font.setBold(False)
                    font.setItalic(False)
                    # font.setWeight(50)
                    self.Number_of_Days.setFont(font)
                    self.Number_of_Days.setFrameShape(QFrame.NoFrame)
                    self.Number_of_Days.setFrameShadow(QFrame.Plain)
                    self.Number_of_Days.setAlignment(Qt.AlignCenter)
                    self.Number_of_Days.setObjectName("Number_of_Days")
                    self.Day_or_Days = QLabel(self.BirthdayFrame)
                    self.Day_or_Days.setGeometry(QRect(820, 36, 101, 31))
                    font = QFont()
                    font.setFamily("Bahnschrift SemiBold")
                    font.setPointSize(14)
                    font.setBold(False)
                    font.setItalic(False)
                    # font.setWeight(50)
                    self.Day_or_Days.setFont(font)
                    self.Day_or_Days.setFrameShape(QFrame.NoFrame)
                    self.Day_or_Days.setFrameShadow(QFrame.Plain)
                    self.Day_or_Days.setAlignment(Qt.AlignCenter)
                    self.Day_or_Days.setObjectName("Day_or_Days")
                    if day_until == 1:
                        print("Equal to one")
                        self.Day_or_Days.setText("Day")
                        self.Number_of_Days.setText(f"{int(row[5])}")
                    if day_until == 0:
                        self.Day_or_Days.setText("TODAY")
                        self.Day_or_Days.setGeometry(QRect(820, 20, 101, 31))
                        self.Number_of_Days.setText("")
                    if day_until != 0 and day_until != 1:
                        self.Day_or_Days.setText("Days")
                        self.Number_of_Days.setText(f"{int(row[5])}")
                    self.ui.verticalLayout_8.addWidget(self.BirthdayFrame)
                    y += 80

            except Exception as e:
                print(f"Error raised when returning all values of Database and making birthday build: {e}")

    def show(self):
        self.main_win.show()
    def showAddUser(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.add_page)
    def showHome(self):
        self.updateHomePage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
    def showSettings(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.setting_page)

    def update_birthday_field(self):
        day = self.ui.calendarWidget.selectedDate()
        # print(self.ui.calendarWidget.selectedDate().toPyDate().day)
        # format like github
        birthday = day.toString('MMMM d, yyyy')

        self.ui.birthday_text.setText(f"Birthday : {birthday}")

        formatted = 'th'
        if day == 1 or day == 21 or day == 31:
            formatted = "st"
        if day == 2 or day == 22:
            formatted = "nd"
        if day == 3 or day == 23:
            formatted = "rd"

    def submitNewPerson(self):
        clear = False
        first_name = self.ui.first_name_text
        last_name = self.ui.last_name_text
        formatted_birthday = self.ui.calendarWidget.selectedDate().toPython()

        if first_name.text() == "":
            first_name.setStyleSheet("border-style: solid; border-color: red; border-width: 3px; border-radius: 10px; ")

        if last_name.text() == "":
            last_name.setStyleSheet("border-style: solid; border-color: red; border-width: 3px; border-radius: 10px; ")

        if first_name.text() != "" and last_name.text() != "":
            clear = True
            first_name.setStyleSheet("border-style: solid; border-color: green; border-width: 3px; border-radius: 10px; ")
            last_name.setStyleSheet("border-style: solid; border-color: green; border-width: 3px; border-radius: 10px; ")
            self.ui.submit_info_btn.setStyleSheet("border-style: solid; border-color: green; border-width: 3px; border-radius: 10px; ")
            self.ui.birthday_text.setStyleSheet("border-style: solid; border-color: green; border-width: 3px; border-radius: 10px; ")

            add_new_birthday(first_name.text(), last_name.text(), formatted_birthday)

        # clears fields and return styles back to normal
        if clear:
            time.sleep(2)
            first_name.setText("")
            last_name.setText("")
            self.ui.birthday_text.setText("Birthday : ")
            first_name.setStyleSheet("border: 3px solid rgb(118, 231, 255); border-radius: 10px;")
            last_name.setStyleSheet("border: 3px solid rgb(118, 231, 255); border-radius: 10px;")
            self.ui.birthday_text.setStyleSheet("border: 3px solid rgb(118, 231, 255); border-radius: 10px;")
            self.ui.submit_info_btn.setStyleSheet("border: 3px solid rgb(118, 231, 255); border-radius: 10px;")

    def check_length(self):
        self.No_Entries_Label = QLabel(self.ui.home_page)
        self.No_Entries_Label.setGeometry(QRect(0, 200, 1061, 101))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.No_Entries_Label.setFont(font)
        self.No_Entries_Label.setAlignment(Qt.AlignCenter)
        self.No_Entries_Label.setObjectName("No_Entries_Label")
        try:
            values = cursor.execute("Select * FROM Birthdays")
            values = values.fetchall()
            if len(values) == 0:
                self.No_Entries_Label.setText("Add a person to get started!")
                self.No_Entries_Label.show() #Should already be showing but....
            if len(values) > 0:
                self.No_Entries_Label.setText("Add a person to get started!")
                self.No_Entries_Label.hide()
        except Exception as e:
            print(f"Error when getting length data from DB : {e}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MAIN_APP()
    main_win.show()
    sys.exit(app.exec())