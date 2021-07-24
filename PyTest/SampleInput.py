'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified Time: 23-07-2021
@Title: Aim of the program is User Registration Problem.
'''

class Sample:
    valid_firstName = [("Naziya",True),("Naz",True)]

    invalid_firstName = [("Na", False),
                      ("naziya", False),
                      ("NAZIYA", False),
                      ("Naz99", False),
                      ("N@ziya", False)]


    valid_lastName = [("Syeda",True),("Syed",True)]

    invalid_lastName = [("Sy", False),
                      ("syeda", False),
                      ("SYEDA", False),
                      ("Sye45", False)]

    
    valid_emails = [("abc10@yahoo.com", True),
                        ("abc-100@yahoo.com", True),
                        ("abc.100@yahoo.com", True),
                        ("abc111@abc.com", True),
                        ("abc-100@abc.net", True),
                        ("abc.100@abc.com.au", True)]

    invalid_emails = [("naziya@.com", False),
                        ("nazi@gmail", False),
                        ("abc..12@gmail.com", False),
                        ("abc123@yahoo.c", False),
                        ("abc@abc@gmail.com", False),
                        (".abc@abc@gmail.com", False)]
    

    valid_phoneNumber = [("91 9876543213",True)]

    invalid_phoneNumber = [("91-793243", False),
                        ("9178654346578", False),
                        ("7865438768", False),
                        ("91   8732126924", False),
                        ("91 876565ab324", False),
                        ("91 8@77*324", False),
                        ("91 0000000000", False)]

    
    valid_password = [("Naziya%6789",True)]

    invalid_password = [("Naziya%jkl",False),("naZi732ok",False),("abcd*65efg",False),("ab#cd*65efg",False)]

