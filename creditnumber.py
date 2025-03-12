creditnumber = input("Enter your 16-digit credit number: ")
# creditnumber = creditnumber[-4:]
print(f"xxxx-xxxx-xxxx-{creditnumber}")
creditnumber = creditnumber[::-1]
print(creditnumber)