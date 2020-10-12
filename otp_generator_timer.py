import datetime
import random

otp=random.randint(100000,999999)
otp=str(otp)
count=0
login=False
print(otp)

endtime=datetime.datetime.now()+datetime.timedelta(seconds=10)
print("Enter OTP:")
while True:
    if datetime.datetime.now() < endtime:
        data = input()
        if len(data) > 1:
            count = count + 1
        if data == otp and len(data) == 6:
            login=True
            break
        if data != otp or len(data) != 6:
            print("Invalid OTP. Try again!")
# for one time option:
        # if len(data) > 1 and count > 0:
        #     print("Access Denied")
        #     break
    if datetime.datetime.now() > endtime:
        print("OTP EXPIRED")
        break

if login:
    print("Login Successful")
if not login:
    print("Login Failed")
