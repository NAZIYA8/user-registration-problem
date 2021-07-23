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

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    getUserInput()        