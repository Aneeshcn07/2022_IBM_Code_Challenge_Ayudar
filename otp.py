import random
from twilio.rest import Client

otp=random.randint(1000,9999)

account_sid="AC53128afb83eb4c2e5b1e0b16bb2d7c0d"

auth_token="a49f429494afe48b7a5cd1b00ba23211"

client=Client(account_sid,auth_token)

msg=client.messages.create(

    body=f"Your OTP is {otp}",
    from_="+19706988090",
    to="+916235581300"


)
