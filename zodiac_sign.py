# Problem Statement:
# Given the birthdate and name of the person,
# you want to create a Python program to determine the corresponding Zodiac sign based on the date.

# Question:
# How can you write a Python program that takes name and birthdate as input
# and outputs the corresponding Zodiac sign and store it in a file using Pandas?


# def zodiac_sign(name,birthdate):
#     data = { }
#     data["name"] = name
#     data["Birthday_date"] = birthdate
#     # data["z_sign"] = 
#     # if
#     columns = ["Name", "DOB"]
#     df = pd.DataFrame([data]) 
#     print(df)
#     df.to_csv("data.csv")

# zodiac_sign("abc","1-05-1447")

# Aries	March 21 – April 19
# Taurus	April 20 – May 20
# Gemini	May 21 – June 20
# Cancer	June 21 – July 22
# Leo	July 23 – August 22
# Virgo	August 23 – September 22
# Libra	September 23 – October 22
# Scorpio	October 23 – November 21
# Sagittarius	November 22 – December 21
# Capricorn	December 22 – January 19
# Aquarius	January 20 – February 18
# Pisces	February 19 – March 20

import pandas as pd
from datetime import datetime

def zodiac_sign(day,month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"


zodiac_sign_list = []
while True:
    name = input("Enter your name: ")
    birthdate = input ("Please enter birthday date in DD-MM-YYYY Format: ")
    dob = datetime.strptime(birthdate, "%d-%m-%Y")
    zodiac = zodiac_sign(dob.day, dob.month)
    print(f'Your name is {name} and zodiac sign is {zodiac}')
    zodiac_sign_list.append({"Name": name, "Birthday": birthdate, "Zodiac-sign": zodiac})

    finder = input("Do you want to find any other zodiac sign (Yes/No)? ")
    if finder.lower() == "yes":
        continue
    else:
        break

dataframe = pd.DataFrame(zodiac_sign_list)
dataframe.to_csv("data.csv",index=False)

print("All data saved in file.")



