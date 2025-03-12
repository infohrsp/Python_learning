username = input("Enter a valid username: ")
if len(username) >12 :
    print("Length >12 ")
    if username.count(" "):
        print("contain space")
    else :
        if not username.isalpha() :
            print("Contain number")
else :
    if username.count(" "):
        print("contain space")
        if not username.isalpha() :
            print("Contain number")
    else :
        if not username.isalpha() :
            print("Contain number")
        else :
            print(f"Welcome {username}")
