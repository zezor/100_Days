import smtplib

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
            to_addrs=sender_email,
            msg=f"Subject:BIRTHDAY MESSAGE!\n\n {message}")