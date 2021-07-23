'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified Time: 23-07-2021
@Title: Aim of the program is User Registration Problem.
'''

from LoggerFormat import logger
import re
from RegexPattern import RegexPattern as re_pattern

class ValidateDetails:


    def validateFirstName(firstNameInput):
        """
    Description:
        This method is used for  validating first name with regex pattern.
    Return:
        It returns valid if its valid first name.
        It returns Invalid if its Invalid first name.
       
    """
        
        try:
            if re.match(re.compile(re_pattern.firstName_pattern),firstNameInput):
                return "Valid"
            else:
                return "Invalid"

        except Exception as err:
            logger.error(err)

    def validateLastName(lastNameInput):
        """
    Description:
        This method is used for  validating last name with regex pattern.
    Return:
        It returns valid if its valid last name.
        It returns invalid if its Invalid last name.
       
    """
        try:
            if re.match(re.compile(re_pattern.lastName_pattern),lastNameInput):
                return "Valid"
            else:
                return "Invalid"

        except Exception as err:
            logger.error(err)
        