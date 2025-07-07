import random
import smtplib
import datetime as dt
from calendar import weekday


def send_email():

    my_email= "kemma2993two@gmail.com"
    password = "embgffhisasvduiy"

    # password = "wvmgmswunletdhdi"
    #

    with smtplib.SMTP("smtp.gmail.com") as connection:  #connecting
        connection.starttls() # securing the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kemma2993@gmail.com",
            msg=F"Subject:MONDAY MOTIVATION!\n\n {quote}")



now = dt.datetime.now()
week_day = now.weekday()

if week_day == 0:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
    send_email()




# try:
#     with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="kemma2993@gmail.com",
#             msg="Subject:Hello!\n\nThis is my email automating app."
#         )
#     print("Email sent successfully.")
# except Exception as e:
#     print("Error:", e)

# now = dt.datetime.now()
# year = now.year
# month = now.month
# week_day = now.weekday()
#
#
# date_of_birth = dt.datetime(year= 1993, month=9 , day=29)

