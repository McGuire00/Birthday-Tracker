import sys
import datetime
import time
import sqlite3

current_date = datetime.datetime.today().date()
current_year = current_date.year
current_time = datetime.datetime.now().strftime("%H:%M:%S")

days_in_year = 365.2425
database = sqlite3.connect('Birthdays.db')
cursor = database.cursor()


#Create Birthday Database
try:
    database.execute("""CREATE TABLE IF NOT EXISTS Birthdays (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        First_Name TEXT NOT NULL,
        Last_Name TEXT NOT NULL,
        Birthdate TEXT NOT NULL,
        Age INTEGER NOT NULL,
        DaysUntilBirthday REAL NOT NULL);""")
    database.commit()
except Exception as e:
    print(f"Error occured when creating Birthdays Database : {e}")

def add_new_birthday(first, last, birthdate):
    age = calculate_age(birthdate)
    days_until_birthday = count_days_until_birthday(birthdate)
    try:
        database.execute("INSERT INTO BIRTHDAYS (First_Name, Last_Name, Birthdate, Age, DaysUntilBirthday) VALUES (:First, :Last, :Birthdate, :Age, :DaysUntilBirthday)", {"First": first, "Last":last, "Birthdate": birthdate, "Age": age, "DaysUntilBirthday":days_until_birthday})
        print(f"{first} {last}. Birthday : {birthdate}. Age : {age}. Days until Birthday : {days_until_birthday}")
        database.commit()
    except Exception as e:
        print(f"Error in adding user to database: {e}")


def count_days_until_birthday(birthdate):
    time_delta = (datetime.date(int(current_year), int(birthdate.month), int(birthdate.day)) - datetime.datetime.today().date())
    num_days_birthday = time_delta.total_seconds() / 60 / 60 / 24
    if num_days_birthday == 0.0:
        num_days_birthday = 0
    elif num_days_birthday < 1.0:
        num_days_birthday = 365 + num_days_birthday
    return int(num_days_birthday)


def calculate_age(birthdate):
    user_birthday = datetime.date(int(birthdate.year), int(birthdate.month), int(birthdate.day))
    current_age = int((current_date - user_birthday).days / days_in_year)
    return current_age

def dbupdate():
    try:
        alldays = cursor.execute("SELECT id, Birthdate, DaysUntilBirthday From Birthdays")
        result = cursor.fetchall()
        for row in result:
            sbirthdate = row[1]
            birthdate = datetime.datetime.strptime(sbirthdate, "%Y-%m-%d").date()
            currentbday = datetime.date(current_year, birthdate.month, birthdate.day)
            Timedelta = datetime.date(current_year, birthdate.month, birthdate.day) - current_date
            NumDaysUntilBirthdays = Timedelta.total_seconds() / 60 /60 /24
            if NumDaysUntilBirthdays < 0 :
                NumDaysUntilBirthdays = 365 + NumDaysUntilBirthdays
            cursor.execute("UPDATE Birthdays SET DaysUntilBirthday = :NumDaysUntilBirthdays WHERE id = :id",    {"NumDaysUntilBirthdays":NumDaysUntilBirthdays, "id": row[0]})
    except Exception as e:
        print(f"Error occured when Updating the Database: {e}")
