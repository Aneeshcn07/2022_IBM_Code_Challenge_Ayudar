import tkinter as tk
import random
from twilio.rest import Client


otp=random.randint(1000,9999)

account_sid="AC53128afb83eb4c2e5b1e0b16bb2d7c0d"

auth_token="#5a211d147bfd16af69f70e9419239c40"

client=Client(account_sid,auth_token)

root= tk.Tk()
canvas = tk.Canvas(root, width = 450, height = 400)
canvas.pack()

def getNumber ():  
    x1 = entry1.get()

    msg=client.messages.create(

    body=f"Your OTP is {otp}",
    from_="+19706988090",
    to=x1
    )
def getOTP ():  
    x2 = entry2.get()
    if x2==str(otp):
        label3 = tk.Label(root, text="Valid ")
        label3.config(fg="green",font=('helvetica', 16))
        canvas.create_window(200,300,window=label3)
    else:
        label3 = tk.Label(root, text="Invalid")
        label3.config(fg="red",font=('helvetica', 16))
        canvas.create_window(200,300,window=label3)



#labels
label1 = tk.Label(root, text='Enter you mobile number:')
# label1.config(font=('helvetica', 14))
canvas.create_window(200, 100, window=label1)
label2 = tk.Label(root, text="Enter your OTP: ")
canvas.create_window(200,200,window=label2)

#inputs
entry1 = tk.Entry (root) 
canvas.create_window(200, 130, window=entry1)
entry2 = tk.Entry (root) 
canvas.create_window(200, 230, window=entry2)

#buttons
button1 = tk.Button(text='Generate OTP',command=getNumber, bg='brown', fg='white')
canvas.create_window(200, 170, window=button1)
button2 = tk.Button(text='Verify',command=getOTP, bg='brown', fg='white')
canvas.create_window(200, 270, window=button2)
    
# button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
# canvas.create_window(200, 180, window=button1)


root.mainloop()
