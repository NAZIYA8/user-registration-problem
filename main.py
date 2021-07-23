'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified Time: 23-07-2021
@Title: Aim of the program User Registration Problem.
'''

from LoggerFormat import logger
from UserDetailsValiation import ValidateDetails

def getUserInput():
    """
    Description:
        This metho is used to get input from the user for valiation.

    """

    try:
        firstName = input("Enter the first Name :")
        logger.info("Entered First Name is {}".format(ValidateDetails.validateFirstName(firstName)))

        lastName = input("Enter the last Name :")
        logger.info("Entered last Name is {}".format(ValidateDetails.validateLastName(lastName)))

        email = input("Enter the email :")
        logger.info("Entered email is {}".format(ValidateDetails.validateEmail(email)))

        mobileNumber = input("Enter the mobile number :")
        logger.info("Entered mobile number is {}".format(ValidateDetails.validateNumber(mobileNumber)))

        password = input("Enter the password :")
        logger.info("Entered password is {}".format(ValidateDetails.validatePassword(password)))

        emailSample = ['abc@yahoo.com', 'abc-100@yahoo.com', 'abc.100@yahoo.com', 'abc111@abc.com',
                        'abc-100@abc.net', 'abc.100@abc.com.au', 'abc@1.com', 'abc@gmail.com.com', 'abc+100@gmail.com']
        email = input("Enter the email :")
        for item in emailSample:
            logger.info("Entered email is {}".format(ValidateDetails.validateEmail(item)))
            break

    except Exception as err:
        logger.error(err)




if __name__ == "__main__":
    getUserInput()        