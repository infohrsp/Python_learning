import time

timer=int(input("Enter time in seconds : "))
for i in range(timer,0,-1) :
    second = timer%60
    minutes = int(timer/60)%60
    hours = int(timer/3600)%3600
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)
    timer-=1
print("Time's UP!")