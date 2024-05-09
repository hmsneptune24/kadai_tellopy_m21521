import socket
import sys
from time import sleep
from tkinter import*


host=''
port=9000
locaddr=(host,port)

tello_ip='192.168.10.1'
tello_port=8889

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(locaddr)

window=Tk()
window.title('Tello')
c=Canvas(window,height=300,width=400)
c.pack()

hat = c.create_oval(170, 120, 230, 180, fill='#0000FF')

def recv():
    count=0
    while True:
        try:
            data,server=sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\nException　です。\n')
            break
                
#Autocommand    
def  tlauto(event):
    sock.sendto(b'takeoff',(tello_ip,tello_port))
    print('takeoff \n')
    sleep(5)
    sock.sendto(b'forward 50',(tello_ip,tello_port))
    print('forward \n')
    sleep(5)
    sock.sendto(b'back 50',(tello_ip,tello_port))
    print('back \n')
    sleep(5)
    sock.sendto(b'forward 50',(tello_ip,tello_port))
    print('forward \n')
    sleep(5)
    sock.sendto(b'back 50',(tello_ip,tello_port))
    print('back \n')
    sleep(5)
    sock.sendto(b'forward 50',(tello_ip,tello_port))
    print('forward \n')
    sleep(5)
    sock.sendto(b'land',(tello_ip,tello_port))
    print('land \n')

#キーボード反応用command
#Auto
c.bind_all('<KeyPress-p>',tlauto)
