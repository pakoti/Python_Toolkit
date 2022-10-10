from tkinter import *
import tkinter as tk



class calc:
    def __init__(self,master):
        self.operator=""
        self.var=StringVar()
        self.root=master
        master.title("Basic Calculator")
        master.geometry("500x500+400+200")
        self.entry = Entry(textvariable=self.var,bg='green',width=45,bd=20,insertwidth=9,justify='right',font=('arial',10))
        self.entry.pack()
        self.t = Text(self.entry,height=40)



        label_key = Label(root, height=15, width=30,bd=10,bg='white')
        label_key.pack(side=LEFT, fill=BOTH, expand=True)

        label_fkey = Label(root, height=15, width=15, bg='white')
        label_fkey.pack(fill=BOTH, expand=True)

        label_7 = Label(label_key, bg='black')
        label_7.grid(row=0, column=0)
        button_7 = Button(label_7, text='7', font=('arian', '16'),command= lambda : self.click_button(7),bg='black',fg='blue')
        button_7.pack()

        label_8 = Label(label_key, bg='black')
        label_8.grid(row=0, column=1, padx=20)
        button_8 = Button(label_8, text='8', font=('arian', '16'),command= lambda: self.click_button(8),bg='black',fg='blue')
        button_8.pack()

        label_9 = Label(label_key, bg='black')
        label_9.grid(row=0, column=2, padx=10)
        button_9 = Button(label_9, text='9', font=('arian', '16'),command= lambda: self.click_button(9),bg='black',fg='blue')
        button_9.pack()

        label_4 = Label(label_key, bg='black')
        label_4.grid(row=1, column=0, padx=10, pady=10)
        button_4 = Button(label_4, text='4', font=('arian', '16'),command= lambda: self.click_button(4),bg='black',fg='blue')
        button_4.pack()

        label_5 = Label(label_key, bg='black')
        label_5.grid(row=1, column=1, padx=10, pady=10)
        button_5 = Button(label_5, text='5', font=('arian', '16'),command= lambda: self.click_button(5),bg='black',fg='blue')
        button_5.pack()

        label_6 = Label(label_key, bg='black')
        label_6.grid(row=1, column=2, padx=10, pady=10)
        button_6 = Button(label_6, text='6', font=('arian', '16'),command= lambda: self.click_button(6),bg='black',fg='blue')
        button_6.pack()

        label_1 = Label(label_key, bg='black')
        label_1.grid(row=2, column=0, padx=10)
        button_1 = Button(label_1, text='1', font=('arian', '16'),command= lambda: self.click_button(1),bg='black',fg='blue')
        button_1.pack()

        label_2 = Label(label_key, bg='black')
        label_2.grid(row=2, column=1, padx=10)
        button_2 = Button(label_2, text='2', font=('arian', '16'),command= lambda: self.click_button(2),bg='black',fg='blue')
        button_2.pack()

        label_3 = Label(label_key, bg='black')
        label_3.grid(row=2, column=2, padx=10)
        button_3 = Button(label_3, text='3', font=('arian', '16'),command= lambda: self.click_button(3),bg='black',fg='blue')
        button_3.pack()

        label_0 = Label(label_key, bg='black')
        label_0.grid(row=3, column=0, padx=10, pady=10)
        button_0 = Button(label_0, text='0', font=('arian', '16'),command= lambda: self.click_button(0),bg='black',fg='blue')
        button_0.pack()

        label_deci = Label(label_key, bg='black')
        label_deci.grid(row=3, column=1, padx=10, pady=10)
        button_deci = Button(label_deci, text='.', font=('arian', '16'),command= lambda: self.click_button('.'),bg='black',fg='blue')
        button_deci.pack()

        label_equal = Label(label_key, bg='black')
        label_equal.grid(row=3, column=2, padx=10, pady=10)
        button_equal = Button(label_equal, text='=', font=('arian', '16'),command= self.evaluate,bg='black',fg='blue')
        button_equal.pack()
        
        label_C = Label(label_fkey, bg='black')
        label_C.grid(row=0, column=0,columnspan=2)
        button_C = Button(label_C, text='C', font=('arian', '16'), height=1, width=10,command=  self.clear,bg='black',fg='blue')
        button_C.pack(side=LEFT)

        label_sub = Label(label_fkey, bg='black')
        label_sub.grid(row=1, column=0, sticky=W, pady=10)
        button_sub = Button(label_sub, text='-', font=('arian', '16'), height=1, width=3,command= lambda: self.click_button('-'),bg='black',fg='blue')
        button_sub.pack(side=LEFT)

        label_mul = Label(label_fkey, bg='black')
        label_mul.grid(row=1, column=1, sticky=E)
        button_mul = Button(label_mul, text='x', font=('arian', '16'), height=1, width=3,command= lambda: self.click_button('*'),bg='black',fg='blue')
        button_mul.pack()

        label_div = Label(label_fkey, bg='black')
        label_div.grid(row=2, column=0, sticky=W)
        button_div = Button(label_div, text='/', font=('arian', '16'), height=1, width=3,command= lambda: self.click_button('/'),bg='black',fg='blue')
        button_div.pack()

        label_add = Label(label_fkey, bg='black')
        label_add.grid(row=2, column=1, sticky=E)
        button_add = Button(label_add, text='+', font=('arian', '16'), height=1, width=3,command= lambda: self.click_button('+'),bg='black',fg='blue')
        button_add.pack()

        label_lbrace = Label(label_fkey, bg='black')
        label_lbrace.grid(row=3,column=0,sticky=W,pady=10)
        button_lbrace = Button(label_lbrace,text='(', font=('arian', '16'), height=1, width=3,command= lambda: self.click_button('('),bg='black',fg='blue')
        button_lbrace.pack()

        label_rbrace = Label(label_fkey, bg='black')
        label_rbrace.grid(row=3, column=1, sticky=E, pady=10)
        button_rbrace = Button(label_rbrace, text=')', font=('arian', '16'), height=1, width=3,command=lambda: self.click_button(')'),bg='black',fg='blue')
        button_rbrace.pack()



    def evaluate(self):
        self.answer =eval(self.entry.get())
        self.var.set(self.answer)
        self.operator = str(self.answer)

    def click_button(self,numbers):
        global operator
        global var
        self.operator = self.operator + str(numbers)
        self.var.set(self.operator)

    def clear(self):
        self.entry.delete(0,END)
        self.operator=""


root=Tk()
if __name__=="__main__":

    app=calc(root)
    root.mainloop()