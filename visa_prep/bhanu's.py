def is_valid_number(number):

    if number.startswith('+') and ' ' in number:
        country_code, phone_number = number.split()
        if len(country_code) == 3 and country_code[0] == '+' and country_code[1:].isdigit():
            if len(phone_number) == 10 and phone_number.isdigit():
                return "Correct"
    if len(number) == 10 and number.isdigit():
        return "Correct"
    return "Incorrect"
number = input().strip()
print(is_valid_number(number))
