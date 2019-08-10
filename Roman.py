"""Roman Numerals Converter"""

# My variables:
sets_of_numerals = (("I", "V", "X"),("X", "L", "C"),("C", "D", "M"))
decimal_number_range = range(1, 1001)
given_number = 0

print("Roman Numerals Converter, reporting in!")
try:
    given_number = input("Please enter an absolute integer from 1 to 1000 to convert to Roman numerals:")
    given_number = int(given_number)
except:
    pass

# My functions:
def split_into_list(given_num):
    """function that splints a number into digits based on the decimal place and puts them into a reverse 
    list"""
    number_string = str(given_num)
    list_of_strings = list(number_string)
    list_of_strings.reverse()
    return list_of_strings

def covert_list_to_roman(our_list):
    """function converts a list of decimal digits into a list of roman numerals"""
    decimal_place = 0
    if len(our_list) == 4 and int(given_number) > 999:
        list_of_roman_numerals.append("M")
    else:
        for decimal_digit in our_list:
            if decimal_digit == "1" :
                decimal_digit = sets_of_numerals[decimal_place][0]
            if decimal_digit == "2" :
                decimal_digit = 2 * sets_of_numerals[decimal_place][0]
            if decimal_digit == "3" :
                decimal_digit = 3 * sets_of_numerals[decimal_place][0]
            if decimal_digit == "4" :
                decimal_digit = sets_of_numerals[decimal_place][0] + sets_of_numerals[decimal_place][1]
            if decimal_digit == "5" :
                decimal_digit = sets_of_numerals[decimal_place][1]
            if decimal_digit == "6" :
                decimal_digit = sets_of_numerals[decimal_place][1] + sets_of_numerals[decimal_place][0]
            if decimal_digit == "7" :
                decimal_digit = sets_of_numerals[decimal_place][1] + 2 * sets_of_numerals[decimal_place][0]
            if decimal_digit == "8" :
                decimal_digit = sets_of_numerals[decimal_place][1] + 3 * sets_of_numerals[decimal_place][0]
            if decimal_digit == "9" :
                decimal_digit = sets_of_numerals[decimal_place][0] + sets_of_numerals[decimal_place][2]
            if decimal_digit == "0" :
                decimal_digit = ""
            list_of_roman_numerals.append(decimal_digit)
            decimal_place +=1
        list_of_roman_numerals.reverse()
    return list_of_roman_numerals

# My program procedure

while given_number is not "q":
    try:
        while int(given_number) not in decimal_number_range:
            print("That is not within the defined parameters")
            given_number = input("Please enter an absolute integer from 1 to 1000 or q to quit:")
        else:
            list_of_digits = split_into_list(given_number)
            list_of_roman_numerals = []
            our_roman_number = "".join(covert_list_to_roman(list_of_digits))
            print(f"The representation of {given_number} in roman numerals is: " + our_roman_number)
            given_number = input("Please enter an absolute integer from 1 to 1000 or q to quit:")
    except:
        print("That is not within the defined parameters")
        given_number = input("Please enter an absolute integer from 1 to 1000 or q to quit:")
        
else:
    print("\nGG")
