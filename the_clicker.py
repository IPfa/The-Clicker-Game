import tkinter as tk
from tkinter import messagebox
from random import randint


def evaluate(event=None):
    global soted_numbers
    target_number = soted_numbers[0]
    button_pressed = event.widget._name.replace("!", "")
    if button_pressed == "button":
        button_pressed = "button1"
    pressed_button_value = globals()[button_pressed].cget("text")
    if target_number == pressed_button_value:
        exec(f'{button_pressed}.config(state=tk.DISABLED)')
        del soted_numbers[0]


def change_time():
    global time_counter
    global soted_numbers
    time_counter += 1
    label.config(text=time_counter)
    if len(soted_numbers) != 0:
        label.after(1000, change_time)
    else:
        messagebox.showinfo(
            title="Congratulations!",
            message=f'Your result is {time_counter} seconds!'
        )
        window.destroy()


window = tk.Tk()
window.title("Clicker")
label = tk.Label(window, text="0", fg="red", font=("Arial", 25))


random_numbers = set()
while len(random_numbers) < 25:
    random_number = randint(1, 999)
    random_numbers.add(random_number)
soted_numbers = sorted(list(random_numbers.copy()))


buttons_names = []
for i in range(1, 26):
    name = str("button" + str(i))
    buttons_names.append(name)
    globals()[name] = tk.Button(window, text=random_numbers.pop())
    exec(f'{name}.bind("<Button-1>", evaluate)')


button_name_index = 0
row = 0
column = [i for i in range(1, 6)]
for i in range(5):
    row += 1
    for i in range(5):
        command = f'{buttons_names[button_name_index]}.grid(column={column[i]}, row={row})'
        button_name_index += 1
        exec(command)
label.grid(column=3, row=6)

time_counter = 0
label.after(1000, change_time)

window.mainloop()
