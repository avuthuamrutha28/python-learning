#Write a program to accept any character from the user; determine whether it is – a letter in the upper case, lower case, digit, or a special symbol. (Hint: Use ASCII values.)
char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
else:
    ascii_val = ord(char)

    if 65 <= ascii_val <= 90:
        print(f"'{char}' is an uppercase letter.")
    elif 97 <= ascii_val <= 122:
        print(f"'{char}' is a lowercase letter.")
    elif 48 <= ascii_val <= 57:
        print(f"'{char}' is a digit.")
    else:
        print(f"'{char}' is a special symbol.")
