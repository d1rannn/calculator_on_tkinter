import tkinter

# root
root = tkinter.Tk()
root.title("Simple Calculator by d1rannn")

# functions
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try: 
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except Exception as e: 
        ac()
        text_result.insert(1.0, f"Error: {str(e)}")

def ac():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def add_percentage():
    global calculation
    try:
        calculation = str(eval(calculation) / 100)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except Exception as e:
        ac()
        text_result.insert(1.0, f"Error: {str(e)}")

def add_decimal_point():
    global calculation
    if "." not in calculation:
        calculation += "."
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

# GUI
text_result = tkinter.Text(root, height=1, width=11, font=("SF Pro", 24))
text_result.grid(columnspan=5)

buttonAC = tkinter.Button(root, height=1, width=1, text="AC", command=ac)
buttonAC.grid(row=2, column=1)

buttonC = tkinter.Button(root, height=1, width=1, text="C")
buttonC.grid(row=2, column=2)

buttonPR = tkinter.Button(root, height=1, width=1, text="%", command=add_percentage)
buttonPR.grid(row=2, column=3)

buttonD = tkinter.Button(root, height=1, width=1, text="/", bg="orange", command=lambda: add_to_calculation("/"))
buttonD.grid(row=2, column=4)

button7 = tkinter.Button(root, height=1, width=1, text="7", command=lambda: add_to_calculation(7))
button7.grid(row=3, column=1)

button8 = tkinter.Button(root, height=1, width=1, text="8", command=lambda: add_to_calculation(8))
button8.grid(row=3, column=2)

button9 = tkinter.Button(root, height=1, width=1, text="9", command=lambda: add_to_calculation(9))
button9.grid(row=3, column=3)

buttonM = tkinter.Button(root, height=1, width=1, text="*", bg="orange", command=lambda: add_to_calculation("*"))
buttonM.grid(row=3, column=4)

button4 = tkinter.Button(root, height=1, width=1, text="4", command=lambda: add_to_calculation(4))
button4.grid(row=4, column=1)

button5 = tkinter.Button(root, height=1, width=1, text="5", command=lambda: add_to_calculation(5))
button5.grid(row=4, column=2)

button6 = tkinter.Button(root, height=1, width=1, text="6", command=lambda: add_to_calculation(6))
button6.grid(row=4, column=3)

buttonM = tkinter.Button(root, height=1, width=1, text="-", bg="orange", command=lambda: add_to_calculation("-"))
buttonM.grid(row=4, column=4)

button1 = tkinter.Button(root, height=1, width=1, text="1", command=lambda: add_to_calculation(1))
button1.grid(row=5, column=1)

button2 = tkinter.Button(root, height=1, width=1, text="2", command=lambda: add_to_calculation(2))
button2.grid(row=5, column=2)

button3 = tkinter.Button(root, height=1, width=1, text="3", command=lambda: add_to_calculation(3))
button3.grid(row=5, column=3)

buttonP = tkinter.Button(root, height=1, width=1, text="+", bg="orange", command=lambda: add_to_calculation("+"))
buttonP.grid(row=5, column=4)

button0 = tkinter.Button(root, height=1, width=6, text="0", command=lambda: add_to_calculation(0))
button0.grid(row=6, column=1, columnspan=2)

button_point = tkinter.Button(root, height=1, width=1, text=",", command=add_decimal_point)
button_point.grid(row=6, column=3)

buttonE = tkinter.Button(root, height=1, width=1, text="=", bg="orange", command=evaluate_calculation)
buttonE.grid(row=6, column=4)

# mainloop
root.mainloop()