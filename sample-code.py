import smtplib
import datetime as dt
import random

# Get current day of the week
now = dt.datetime.now()
day_of_week = now.weekday()

# Define the sender's email and password
my_email = "prungsakullikit@gmail.com"
password = "abc1234()" # placeholder

# Read quotes from file
try:
    with open("quotes.txt", "r") as file:
        quotes = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print("Error: `quotes.txt` file not found.")
    quotes = []

# Send email only if it's Tuesday and quotes list is not empty
if day_of_week == 1:
    random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection: # Create an SMTP connection to Gmail's server
        connection.starttls() # Upgrade the connection to a secure encrypted SSL/TLS connection

        # Log in to the email account
        connection.login(user=my_email, password=password)

        # Send an email
        connection.sendmail(
            from_addr=my_email, # Sender's email address
            to_addrs="prungsakullikit@yahoo.com", # Receiver's email address
            msg=f"Subject:Tuesday Motivation\n\n{random_quote}"  # Email subject and body (double newline separates them)
        )

# Close the connection to free up resources
# Instead of using `close()` we can add with in front of `smtplib.SMTP`
# connection.close()



