forbidden_word = "nigga"
while True:
    user_input = input("Enter a string:")
    if user_input.isalpha():
        if forbidden_word not in user_input.lower():
            print("Output:",user_input[::-1])
            break
        else:
            print("Error Reported! Enter a different text.")
    else:
        print("Error Reported! Enter text only.")