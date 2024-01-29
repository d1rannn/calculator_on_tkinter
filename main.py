import tkinter
import tkinter.messagebox

# root
root = tkinter.Tk()
root.title("Simple Calculator by d1rannn")

# functions
def ac():
    try:
        empty_text = ''
        entry_display.delete(0, tkinter.END)
    except Exception as e:
        print(e)


def add_number(number):
    current_text = entry_display.get()
    entry_display.delete(0, tkinter.END)
    entry_display.insert(0, current_text + str(number))
        


# GUI
entry_display = tkinter.Entry(root)
entry_display.pack()

frame_nums1 = tkinter.Frame(root)
frame_nums1.pack()

buttonAC = tkinter.Button(frame_nums1, height=1, width=1, text="AC", command=ac())
buttonAC.pack(side=tkinter.LEFT)

buttonPM = tkinter.Button(frame_nums1, height=1, width=1, text="+/-")
buttonPM.pack(side=tkinter.LEFT)

buttonPR = tkinter.Button(frame_nums1, height=1, width=1, text="%")
buttonPR.pack(side=tkinter.LEFT)

buttonD = tkinter.Button(frame_nums1, height=1, width=1, text="/", bg="orange")
buttonD.pack(side=tkinter.LEFT)

frame_nums789 = tkinter.Frame(root)
frame_nums789.pack()

button7 = tkinter.Button(frame_nums789, height=1, width=1, text="7", command=lambda: add_number(7))
button7.pack(side=tkinter.LEFT)

button8 = tkinter.Button(frame_nums789, height=1, width=1, text="8", command=lambda: add_number(8))
button8.pack(side=tkinter.LEFT)

button9 = tkinter.Button(frame_nums789, height=1, width=1, text="9", command=lambda: add_number(9))
button9.pack(side=tkinter.LEFT)

buttonM = tkinter.Button(frame_nums789, height=1, width=1, text="*", bg="orange")
buttonM.pack(side=tkinter.LEFT)

frame_nums456 = tkinter.Frame(root)
frame_nums456.pack()

button4 = tkinter.Button(frame_nums456, height=1, width=1, text="4", command=lambda: add_number(4))
button4.pack(side=tkinter.LEFT)

button5 = tkinter.Button(frame_nums456, height=1, width=1, text="5", command=lambda: add_number(5))
button5.pack(side=tkinter.LEFT)

button6 = tkinter.Button(frame_nums456, height=1, width=1, text="6", command=lambda: add_number(6))
button6.pack(side=tkinter.LEFT)

buttonM = tkinter.Button(frame_nums456, height=1, width=1, text="-", bg="orange")
buttonM.pack(side=tkinter.LEFT)

frame_nums123 = tkinter.Frame(root)
frame_nums123.pack()

button1 = tkinter.Button(frame_nums123, height=1, width=1, text="1", command=lambda: add_number(1))
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(frame_nums123, height=1, width=1, text="2", command=lambda: add_number(2))
button2.pack(side=tkinter.LEFT)

button3 = tkinter.Button(frame_nums123, height=1, width=1, text="3", command=lambda: add_number(3))
button3.pack(side=tkinter.LEFT)

buttonP = tkinter.Button(frame_nums123, height=1, width=1, text="+", bg="orange")
buttonP.pack(side=tkinter.LEFT)

frame_nums0 = tkinter.Frame(root)
frame_nums0.pack()

button0 = tkinter.Button(frame_nums0, height=1, width=6, text="0", command=lambda: add_number(0))
button0.pack(side=tkinter.LEFT)

button_point = tkinter.Button(frame_nums0, height=1, width=1, text=",")
button_point.pack(side=tkinter.LEFT)

buttonE = tkinter.Button(frame_nums0, height=1, width=1, text="=", bg="orange")
buttonE.pack(side=tkinter.LEFT)

# mainloop
root.mainloop()