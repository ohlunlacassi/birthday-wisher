##################### Normal Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

# Get today's date
# HINT 1: Create a tuple from today's month and day using datetime. e.g.today = (today_month, today_day)
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

# Define the sender's email and password
my_email = "prungsakullikit@gmail.com"
password = "abc1234()" # placeholder

# Read CSV and create a dictionary from it
# HINT 2: Use pandas to read the birthdays.csv
df = pd.read_csv("birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv.
# Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }
birthdays_dict = {
    (row["month"], row["day"]): row for index, row in df.iterrows()
}

# Load letter templates
#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
letters = []

try:
    with open("letter_templates/letter_1.txt") as file1, open("letter_templates/letter_2.txt") as file2, open("letter_templates/letter_3.txt") as file3:
        letters.append(file1.read())
        letters.append(file2.read())
        letters.append(file3.read())
except FileNotFoundError:
    print("File Not Found")

# Check if today matches a birthday if there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    name = birthday_person["name"]
    to_email = birthday_person["email"]

    # Choose a random letter and replace [NAME] with actual name
    random_letter = random.choice(letters).replace("[NAME]", name)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Happy Birthday\n\n{random_letter}"
        )



