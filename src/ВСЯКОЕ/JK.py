import tkinter as tk
main = tk.Tk()
main.geometry('400x400')
main.title("Облако входа")
main.configure(bg='black')

def click():
    print("Вы вошли")

button = tk.Button(main, text="Войти", command=click)
button.pack()
button.place(x=180,y=160)
button.configure(bg='yellow')

main.mainloop()
