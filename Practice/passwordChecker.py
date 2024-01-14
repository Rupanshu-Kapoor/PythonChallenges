import string


def pasCheck(strig: str):
    pass_length = 16
    dict_key = ("is_digit", "is_special", "is_long", "is_upper", "is_lower")
    dict_value = False
    error_dict = dict.fromkeys(dict_key, dict_value)
    error_message_dict = {
        "is_digit": "Please enter a digit ",
        "is_special": "Please enter a special character",
        "is_long": "Please enter at least 8 digit password ",
        "is_upper": "Please enter a upper letter",
        "is_lower": "Please enter a lower letter"
    }
    if len(strig) >= pass_length:
        error_dict["is_long"] = True

    for i in strig:
        if i in string.punctuation:
            error_dict["is_special"] = True
        elif i.isupper():
            error_dict["is_upper"] = True
        elif i.isdigit():
            error_dict["is_digit"] = True
        elif i.islower():
            error_dict["is_lower"] = True

        if all(error_dict.values()):
            print("Password is strong")
            break
    else:
        print("Invalid Password")
        for i, y in error_dict.items():
            if not y:
                print(error_message_dict[i])


pasCheck("j4ea5a")
