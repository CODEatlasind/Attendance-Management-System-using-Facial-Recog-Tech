import yagmail
import pandas
import datetime as dt


# Add sender account to sender(as a string) and Add the password to pwd(as a string)
sub = """Attendance!"""

yag = yagmail.SMTP(user=sender, password=pwd)

df = pandas.read_csv("C:\Attendance_Tracker\mail_list.csv")


def dispatch_Email():
    for index, row in df.iterrows():
        body = [f"""
    Hello {row['name']},
    Attendance for today, i.e., 
    {dt.datetime.now().date()} ({dt.datetime.now().strftime('%A')}), is attached herewith.
    """, f"{row['attachment']}"]
        yag.send(to=row["email"], subject="Attendance!", contents=body)
        print("Email Dispatched! Attendance Sharing Successful!!")

