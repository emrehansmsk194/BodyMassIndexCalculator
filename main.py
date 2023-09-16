from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=350, height=230)

label = Label(text="Enter Your Weight(kg)",font=("Arial", 9, "normal"))
label.place(x=120,y=30)

entry = Entry(width=15)
entry.focus()
entry.place(x=130,y=50)

label2 = Label(text="Enter Your Height(cm)",font=("Arial", 9, "normal"))
label2.place(x=120, y=70)
label2.config(pady=5)

entry2 = Entry(width=15)
entry2.place(x=130, y=95)
result_label = Label(font=("Arial", 9, "normal"))
result_label.place(x=120, y=150)
result_label.config(pady=5)

def button_clicked():
    try:
        weight = int(entry.get())
        height = int(entry2.get()) / 100
        bmi = weight / (height * height)
        if bmi < 18.5:
            result_label.config(text=f"Your BMI is {round(bmi,2)}. You are in underweight.")
            result_label.place(x=20, y=150)
            result_label.config(pady=5)
        elif bmi < 25.0:
            result_label.config(text=f"Your BMI is {round(bmi,2)}. You are normal weight.")
            result_label.place(x=20, y=150)
            result_label.config(pady=5)
        elif bmi < 30.0:
            result_label.config(text=f"Your BMI is {round(bmi,2)}. You are in overweight.")
            result_label.place(x=20, y=150)
            result_label.config(pady=5)
        else:
            result_label.config(text=f"Your BMI is {round(bmi,2)}. You are obese.")
            result_label.place(x=20, y=150)
            result_label.config(pady=5)
    except ValueError:
        result_label.config(text="Enter a valid number")
        result_label.place(x=120, y=150)
        result_label.config(pady=5)





button = Button(text="Calculate",command=button_clicked)
button.place(x=145, y=120)



window.mainloop()