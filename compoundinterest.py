principal = -1
rate = -1
time =-1
while  principal<0  :
    print("Enter a valid amount: ")
    principal = float(input())
while  rate<0:
    print("Enter a valid rate : ")
    rate = float(input())
while  time<0:
    print("Enter a valid time(years): ")
    time = float(input())

amount = principal* pow(1+rate/100, time)
print(f"You have Rs.{amount:.2f}")