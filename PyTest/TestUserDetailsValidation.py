'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified Time: 24-07-2021
@Title: Aim of the program is User Registration Problem.
'''


from UserDetailsValiation import ValidateDetails as validate
from SampleInput import Sample as sample
import pytest


## Test cases for the first name
@pytest.mark.name
@pytest.mark.parametrize("firstNameInput,expected",sample.valid_firstName)
def test_validName(firstNameInput,expected):
    """
Description:
    The given valid name should return true in test case
Parameter:
    It takes name_input and expected as a parameter.
"""
    assert validate.validateFirstName(firstNameInput) == expected


@pytest.mark.name
@pytest.mark.parametrize("invalid_firstName,expected",sample.invalid_firstName)
def test_invalidName(invalid_firstName,expected):
    """
Description:
    The given invalid name should return false in test case
Parameter:
    It takes invalid_name and expected as a parameter..
"""
    assert validate.validateFirstName(invalid_firstName) == expected


## Test cases for last name

@pytest.mark.name
@pytest.mark.parametrize("lastNameInput,expected",sample.valid_lastName)
def test_validName(lastNameInput,expected):
    """
Description:
    The given valid name should return true in test case
Parameter:
    It takes name_input and expected as a parameter.
"""
    assert validate.validateLastName(lastNameInput) == expected


@pytest.mark.name
@pytest.mark.parametrize("invalid_lastName,expected",sample.invalid_lastName)
def test_invalidName(invalid_lastName,expected):
    """
Description:
    The given invalid name should return false in test case
Parameter:
    It takes invalid_name and expected as a parameter..
"""
    assert validate.validateLastName(invalid_lastName) == expected
   

 # Test cases For Email 

@pytest.mark.email
@pytest.mark.parametrize("valid_email,expected",sample.valid_emails)
def test_validEmail(valid_email,expected):
    """
Description:
    The given valid email should return true in test case
Parameter:
    It takes valid_email and expected as a parameter.
"""

    assert validate.validateEmail(valid_email) == expected


@pytest.mark.email
@pytest.mark.parametrize("invalid_emails,expected",sample.invalid_emails)
def test_invalidEmail(invalid_emails,expected):
    """
Description:
    The given invalid Email should return false in test case
Parameter:
    It takes invalid_email_input and expected as parameter.
"""
    assert validate.validateEmail(invalid_emails) == expected

## Test cases For Phone Number

@pytest.mark.phonenumber
@pytest.mark.parametrize("phoneNumberInput,expected", sample.valid_phoneNumber)
def test_validPhoneNumber(phoneNumberInput,expected):
    """
Description:
    The given valid Phone number should return true in test case
Parameter:
    It takes phone_number_ input and expected as a parameter.
"""
    assert validate.validateNumber(phoneNumberInput) == expected


@pytest.mark.phonenumber
@pytest.mark.parametrize("invalid_phoneNumber,expected",sample.invalid_phoneNumber)
def test_invalidPhoneNumber(invalid_phoneNumber,expected):
    """
Description:
    The given invalid phone number should return false in test case
Parameter:
    It takes invalid_phone number and expected as a parameter
"""
    assert validate.validateNumber(invalid_phoneNumber) == expected
   

## Test cases For Password

@pytest.mark.password
@pytest.mark.parametrize("passwordInput,expected",sample.valid_password)

def test_validPassword(passwordInput,expected):
    """
Description:
    The given valid Password should return true in test case
Parameter:
     It takes valid_password and expected as a parameter
"""
    assert validate.validatePassword(passwordInput) == expected
    

@pytest.mark.password
@pytest.mark.parametrize("invalid_passwordInput , expected",sample.invalid_password)

def test_invalidPassword(invalid_passwordInput,expected):
    """
Description:
    The given invalid Password should return false in test case
Parameter:
    It takes invalid_password and expected as a parameter
"""

    assert validate.validatePassword(invalid_passwordInput) == expected
