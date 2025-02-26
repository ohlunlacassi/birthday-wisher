# Automated Email Scripts

This repository contains two Python scripts that automate email sending for different purposes:

1. **Motivational Quote Email**: This scripts sends a random motivational quote to a specified email address.

   **How It Works**:
      1. Reads the current day of the week
      2. If it's Tuesday, the script reads quotes from `quotes.txt`
      3. Selects a random quote and sends it via email
   
2. **Birthday Greeting Email**: This script sends an automated birthday email with a randomly choosen letter template.
   **How It Works**:
   1. Reads the current date (month and day).
   2. Loads birthday data from `birthdays.csv`
   3. If today matches a birthday, selects a random letter template.
   4. Replaces the placeholder [NAME] with the recipient's actual name.
   5. Send the birthday email

## Configurations
Modify the following variables in the script.

`my_email = "your_email@gmail.com"`

`password = "your_app_password"`  # Use an App Password instead of your real password

`to_email = "recipient_email@example.com"`
            