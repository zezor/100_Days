import smtplib
import datetime as dt




# my_email= "emmanuelnyamekyenti@gmail.com"
# password = "wvmgmswunletdhdi"
#
#
# # with smtplib.SMTP("smtp.gmail.com") as connection:  #connecting
# #     connection.starttls() # securing the connection
# #     connection.login(user=my_email, password=password)
# #     connection.sendmail(
# #         from_addr=my_email,
# #         to_addrs="kemma2993@gmail.com",
# #         msg="Subject:Hello!\n\n This is my email automating app")
#
#
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

now = dt.datetime.now()
print(now)