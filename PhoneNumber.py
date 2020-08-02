#Write a program that cleans up user-entered phone numbers so that they can be sent SMS messages.

#The rules are as follows:

#If the phone number is less than 10 digits assume that it is bad number
#If the phone number is 11 digits and the first number is not 1, then it is a bad number
#If the phone number is more than 11 digits assume that it is a bad number
#You are provided with a class Phone which has following methods:

#number Returns the number that is initialized if the number is valid, following above rules
#INPUT:
#number = Phone("(123) 456-7890").number
#OUTPUT:
#"1234567890"
#This should return "0000000000" if the number is invalid.

#area_code
#Returns an area code from the number. The area code will be 3 digits
#INPUT:
#number = Phone("1234567890")
#number.area_code()
#OUTPUT:
#"123"
#This should be returned as a string.

#pretty
#Returns a neat format of the number with the area code in brackets.
#INPUT:
#number = Phone("1234567890")
#number.pretty()
#OUTPUT:
#"(123) 456-7890"


#MY SOLUTION: 

class Phone:
    
    def __init__(self, phone_number):
        phone = "".join(x for x in phone_number if x.isdigit())
        if len(phone) == 10:
            pass
        elif len(phone) == 11 and phone[0] == "1":
            phone = phone[1:11]
        else:
            phone = "0000000000"
        self.number = phone
        self.area = phone[:3]
        self.pretty_format = "({}) {}-{}".format(phone[:3], phone[3:6], phone[6:])

    def area_code(self):
        return self.area

    def pretty(self):
        return self.pretty_format