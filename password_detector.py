right_password="9876"
attempts = 0
while True:
    guessed_password = input("Enter the password: ")
    attempts += 1

    if guessed_password == right_password:
        print("Password is correct.")
        break
    else:
        if attempts >= 3:
            print("Too many attempts. Device locked for 2 mins.")
            break
        else:
            print(f"Wrong password. Try Again. You have {3 - attempts} attempts left.")