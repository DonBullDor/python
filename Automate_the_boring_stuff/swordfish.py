while True:
    print("login")
    name = input()
    if name != "med":
        continue
    print("enter password")
    password = input()
    if password == "swordfish":
        break

print("Access granted")
