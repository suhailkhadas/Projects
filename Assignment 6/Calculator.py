from tkinter import *

window = Tk()

window.title("Calculator")
window.geometry("320x340")
window.config(bg="#202020")
frame_1=Frame(window,  width=320, height=50, background="white")

menu= Menu (window)

file= Menu(menu, tearoff=0)
file.add_command(label="Exit", command=window.quit)
file.add_separator()
file.add_command(label="Help")
menu.add_cascade(label="File", menu=file)
window.config(menu=menu)

output = Entry(frame_1,width=20,borderwidth=5,background="#202020", fg="white",font=("Arial", 30))

def click(num):
    result=output.get()
    output.delete(0, END)
    output.insert(0, str(result)+ str(num))
def clear():
    output.delete(0,END)

def add():
    n1=output.get()
    global math
    math = "addition"
    global i
    i= int(n1)
    output.delete(0,END)
    
def sub():
    n1=output.get()
    global math
    math = "Sub"
    global i
    i= int(n1)
    output.delete(0,END)
def mul():
    n1=output.get()
    global math
    math = "mul"
    global i
    i= int(n1)
    output.delete(0,END)
def div():
    n1=output.get()
    global math
    math = "div"
    global i
    i= int(n1)
    output.delete(0,END)
def equal():
    n2=int(output.get())
    output.delete(0,END)

    if math== "addition":
        output.insert(0,i+n2)
    elif math=="Sub":
        output.insert(0,i- n2)    
    elif math=="mul":
        output.insert(0,i*n2)
    elif math=="div":
        output.insert(0,i/n2)        
    

frame_2=Frame(window, bg="#202020", width=320, height=370)
num_1=Button(frame_2, text="1" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click(1))
num_2=Button(frame_2, text="2" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click(2))
num_3=Button(frame_2, text="3" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click(3))
num_4=Button(frame_2, text="4" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click(4))
num_5=Button(frame_2, text="5" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click(5))
num_6=Button(frame_2, text="6" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click(6))
num_7=Button(frame_2, text="7" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click(7))
num_8=Button(frame_2, text="8" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click(8))
num_9=Button(frame_2, text="9" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click(9))
num_equal=Button(frame_2, text="=" ,bg="#323232", width="10", height="3", fg="white", command=lambda:equal())
num_add=Button(frame_2, text="+" ,bg="#323232", width="10", height="3", fg="white", command=lambda:add())
num_sub=Button(frame_2, text="-" ,bg="#323232", width="10", height="3", fg="white", command=lambda:sub())
num_0=Button(frame_2, text="0" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click(0))
num_dot=Button(frame_2, text="." ,bg="#323232", width="10", height="3", fg="white", command=lambda:click())
num_neg=Button(frame_2, text="-/+" ,bg="#323232", width="10", height="3", fg="white", command=lambda:click())
num_mull=Button(frame_2, text="x" ,bg="#323232", width="10", height="3", fg="white", command=lambda:mul())
num_div=Button(frame_2, text="/" ,bg="#323232", width="10", height="3", fg="white", command=lambda:div())
num_clear=Button(frame_2, text="Clear" ,bg="#323232", width="10", height="3", fg="white", command=lambda:clear())

num_1.grid(row=2,column=1)
num_2.grid(row=2,column=2)
num_3.grid(row=2,column=3)
num_4.grid(row=3,column=1)
num_5.grid(row=3,column=2)
num_6.grid(row=3,column=3)
num_7.grid(row=4,column=1)
num_8.grid(row=4,column=2)
num_9.grid(row=4,column=3)
num_equal.grid(row=5,column=4)
num_add.grid(row=4,column=4)
num_sub.grid(row=3,column=4)
num_neg.grid(row=5,column=1)
num_0.grid(row=5,column=2)
num_dot.grid(row=5,column=3)
num_mull.grid(row=2,column=4)
num_div.grid(row=1,column=4)
num_clear.grid(row=1,column=3)
output.grid(row=1, column=0)
frame_1.pack(side=TOP)
frame_2.pack(side=BOTTOM)
window.mainloop()
