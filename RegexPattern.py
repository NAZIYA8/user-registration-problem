'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified Time: 23-07-2021
@Title: Aim of the program is User Registration Problem.
'''

class RegexPattern:

    firstName_pattern = "^[A-Z]{1}[a-z]{3,}"
    lastName_pattern = "^[A-Z]{1}[a-z]{3,}"
    email_pattern = "^[a-zA-Z0-9]+([+.-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+[.][a-zA-Z]{2,4}([.][a-zA-Z]{2,4})?"
    mobileNumber_pattern = "^[0-9]{2}\\s{1}[0-9]{10}"