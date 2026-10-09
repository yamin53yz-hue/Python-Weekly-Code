correct_username = "admin"
correct_password = "1234"

attempts = 0
logged_in = False

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        print("Welcome back.")
        logged_in = True
        break
    else:
        print("Invalid username or password.")
        attempts = attempts + 1

if not logged_in:
    print("Too many failed attempts. Goodbye.")