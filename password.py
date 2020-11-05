import random, string

def run():
    initialise = True

    while initialise:

        letters = int(input("Enter number of letters you want: "))
        digits = int(input("Enter the number of digits you want: "))
        special = int(input("Enter the number of special characters you want: "))


        password_count = letters + digits + special

        if password_count >= 6:
            print("The length of your password is: ",password_count)
            password = generate_password(letters, digits, special)
            print(password)
            initialise = False


        else:
            print("The length of your password is less than 6 and is: ",password_count)
            initialise = True


def generate_password(letters, digits, special):
    alphabets = generate_letters(letters)
    numbers = generate_numbers(digits)
    characters = generate_special(special)
    password = alphabets+numbers+characters
    new_password = shuffleAll(password)

    return new_password


def generate_letters(letters):
    text = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase) for n in range(letters)])
    new_letters = shuffleAll(text)
    return new_letters


def generate_numbers(digits):
    text = ''.join([random.choice(string.digits) for n in range(digits)])
    new_digits = shuffleAll(text)
    return new_digits


def generate_special(special):
    text = ''.join([random.choice("~`!@#$%^&':;,.*()_-/") for n in range(special)])
    new_special = shuffleAll(text)
    return new_special


def shuffleAll(text):
    text = list(text)
    random.shuffle(text)
    new_ = ''.join(text)

    return new_


run()
