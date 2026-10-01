def count_cases(text):
    upper_count = 0
    lower_count = 0

    for character in text:
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1

    print (f"There's {upper_count} upper cases and {lower_count} lower cases")

count_cases("Hello World")