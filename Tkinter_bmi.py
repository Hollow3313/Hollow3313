import tkinter

#window

window = tkinter.Tk()
window.title("BMI Calculater")
window.minsize(width=300, height=300)

#label
Label = tkinter.Label(text="Enter Your Weigh (kg)")
Label.config(font=("arial", 10, "bold"))
Label.update()
Label.pack()
Label.config(padx=25, pady=25)

#entry


def entry_input():
    try:
        Input0 = Entry.get()
        Input1 = Entry_1.get()
        bmi  =  float(Input0) / float(Input1) ** 2
        print(bmi)

        if bmi <= 18.4:
            print("underweight")
            Label_underweight.pack()
            Label_try.destroy()

        elif 18.4 < bmi <= 24.9:
            print("normal")
            Label_normal.pack()
            Label_try.destroy()
        elif 24.9 < bmi <= 39.9:
            print("overweight")
            Label_overweight.pack()
            Label_try.destroy()
        else:
            print("obese")
            Label_obese.pack()
            Label_try.destroy()
    
    except:
        print("try agan")
        Label_try.pack()







    


Entry = tkinter.Entry()
Entry.pack()



#label_1
Label_1 = tkinter.Label(text="Enter Your Height (cm)")
Label_1.config(font=("arial", 10, "bold"))
Label_1.pack()
Label_1.config(padx=25, pady=25)
#entry_1
Entry_1 = tkinter.Entry()
Entry_1.pack()

#button
button = tkinter.Button(text="Calculate", command=entry_input)
button.place(x=150-54, y=150-12+80)
button.config(padx=25, pady=0)

button.update()
print(button.winfo_width(), button.winfo_height())

#label series
Label_underweight = tkinter.Label(text="underweight")
Label_underweight.config(padx=10, pady=10)
Label_normal = tkinter.Label(text="normal")
Label_normal.config(padx=10, pady=10)
Label_overweight = tkinter.Label(text="overweight")
Label_overweight.config(padx=10, pady=10)
Label_obese = tkinter.Label(text="obese")
Label_obese.config(padx=10, pady=10)
Label_try = tkinter.Label(text="try agan")
Label_try.config(padx=10, pady=10)






window.mainloop()