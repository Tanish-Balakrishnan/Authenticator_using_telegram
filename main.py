
import requests,random,string
from tkinter import *
import time
import socket   
import platform 
f = open("log.txt", "r")
pp = str(f.read()).split()
res =""
q= " "
            

def otp_checkbox():
    Label(win, text='Password').grid(row=3)
    redbutto = Button(win, text = 'OTP CHECK', fg ='red',command=otp_check)
    e3.grid(row=5,column=0, pady = 2)
    
    # print(q)
    redbutto.grid(row=5,column=1 )

def otp_get():
    q=e3.get()
       

def otp():
    send_otp(pp)
def send_message(mes):
        bot_id = '5473113715:AAFpv7j9PjaZsSG9UfcmND1fZamsVdFjB6o'
        chat_id='-640490861'  
        requests.post("https://api.telegram.org/bot" + bot_id +"/sendMessage?chat_id=" + chat_id +"&text=" + mes) 

def send_otp(pp):
    a = False
    b = False
    
    user = str(e1.get())
    ps = str(e2.get())
    

    if(str(user) == str(pp[0]) and str(ps) == str(pp[1]) ):
        
        global res
        res = ''.join(random.choices(string.digits  ,k=6))
        # print(res)
        mes = "New login initiated, your otp is "+str(res)+"\n\nThis code can be used to log in to your application."+"\n\nIf you didn't request this code by trying to log in on another device, simply ignore this message."
        send_message(mes)
 
            
        otp_checkbox()
        
       
        
        
    else:
        label1 = Label(win, text='Wrong password',fg ='red' )
        label1.grid(row=4)
        
        
def otp_check():
    a = e3.get().split()

    if (str(res) == str(a[0]) ):
        # print(res)
        hostname=socket.gethostname() 
        IPAddr=socket.gethostbyname(hostname)
        m=("Drear "+pp[0]+", We detected a login into your account on "+time.strftime("%H:%M:%S", time.localtime())+"\nThe ip-address of the login device is : "+str(IPAddr)+"\nDEVICE: "+str(platform.platform()))

            
        send_message(m)
        Label(win, text='Login successful').grid(row=6)
    else:
        Label(win, text='Login unsuccessful').grid(row=6)
        print("error")
        time.sleep(5)


win = Tk()
win.title("Login")
win.geometry("500x300")
Label(win, text='User Name').grid(row=2)
Label(win, text='Password').grid(row=3)
lbutton = Button(win, text = 'Login', fg ='red',command=otp)
e1 = Entry(win)
e2 = Entry(win)
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3 = Entry(win)
lbutton.grid(row=4,column=1 )

win.mainloop()

