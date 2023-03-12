import time
s = 0
m = 0
h = 0
num = 0
# times = float(input("enter the hours:"))
while True:
    times = input("enter the time:").split(":")
    if (len(times) != 3):
        print("time format is wrong")
        continue
    clock = [int(times[0]), int(times[1]), int(times[2])]
    if (clock[2] >= 60 or clock[1] >= 60):
        print("time format is wrong")
    else:
        break
while True :
    while s <= 60 :
        wait = time.sleep(1)
        s = s+1
        if s == 60 :
            s = 0
            m = m+1
            if m == 60 :
                m = 0
                h = h+1
        print(str(h)+":"+str(m)+":"+str(s))
        if h == clock[0] and m == clock[1] and s == clock[2]:
            print("THE TIME IS FINISHED")
            exit(0)
# while True:
#     while s <= 60:
#         wait = time.sleep(1)
#         s = s+1
#         print("second:"+str(s))
#         if s == 60 :
#             s = 0
#             m = m+1
#             print("_________________")
#             print("second:"+str(s))
#             print("minute:"+str(m))
#             print("hour:"+str(h))
#             print("_________________")
#             if m == 60 :
#                 m = 0
#                 h = h+1
#                 print("_________________")
#                 print("second:"+str(s))
#                 print("minute:"+str(m))
#                 print("hour:"+str(h))
#                 print("_________________")
#         if times <= (h + m / 60 + s / 3600):
#             print("THE TIME IS FINISHED")
#             exit(0)
    
    
    

