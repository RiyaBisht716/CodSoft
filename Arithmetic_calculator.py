from tkinter import *

window = Tk()
window.title("Arithmetic calculator")
window.geometry('800x300')

def calculate():
    try:
        n1= float(entry1.get())
        n2= float(entry2.get())
    except ValueError:
        answer_label.config(text="Please enter valid numbers")
        return

    operation = operation_var.get()
    
    if operation == "+":
        answer = n1 + n2
    elif operation == "-":
        answer = n1 - n2
    elif operation == "*":
        answer = n1 * n2
    elif operation == "/":
        if n2 ==0:
            answer_label.config(text= " Cannot divide by zero")
            return
        answer = n1/n2
    else:
        answer_label.config(text= "Please select an operation ")
        return



    answer_label.config(text= f"Answer: {answer}")




label1 = Label(window, text = "Number 1:")
label1.grid(row= 0 ,column = 0 ,padx= 10 ,pady= 5)


entry1 = Entry (window)
entry1.grid(row =0 ,column = 1, padx= 10 ,pady = 5)



label2= Label(window ,text= "Number 2:")
label2.grid(row =1 ,column = 0 ,padx = 10 ,pady =5)

entry2= Entry(window)
entry2.grid(row = 1, column = 1,padx =10 ,pady =5)


operation_var = StringVar()
operation_var.set("+")

label3= Label(window, text ="Operation:")
label3.grid(row= 2,column = 0 ,padx= 10,pady =5)


operations_frame =Frame(window)
operations_frame.grid(row= 2,column= 1 ,padx =10, pady = 5)

radio_add = Radiobutton(operations_frame, text ="+", variable= operation_var ,value= "+")
radio_add.pack(side=LEFT)

radio_sub = Radiobutton(operations_frame, text = "-" ,variable= operation_var ,value ="-")
radio_sub.pack(side=LEFT)

radio_multiply =Radiobutton(operations_frame, text = "*" ,variable = operation_var ,value ="*")
radio_multiply.pack(side=LEFT)

radio_divide = Radiobutton(operations_frame, text = "/", variable = operation_var ,value = "/")
radio_divide.pack(side=LEFT)

submit_button = Button(window ,text= "Calculate", command =calculate)
submit_button.grid(row=3 ,column = 0 ,columnspan =2,pady=10)

answer_label = Label(window, text= "Answer: ")
answer_label.grid(row= 4, column = 0, columnspan = 2, pady =5)


window.mainloop()
        
        
