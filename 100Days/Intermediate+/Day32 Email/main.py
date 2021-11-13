import smtplib




import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day


if now.weekday() == 4:
    my_email = "newjoker6@gmail.com"
    password = "ytpcvdqpzcwoioik"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="newjoker6@asia-mail.com", msg="Subject:asuh\n\nbitch ass")
    connection.close()
    print("Mail Sent")