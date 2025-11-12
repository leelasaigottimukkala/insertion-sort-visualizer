import time
from tkinter import *
from tkinter import simpledialog

root = Tk()
root.title("Insertion Sort Visualizer")
root.geometry("700x500")

canvas = Canvas(root, width=650, height=320, bg="white")
canvas.pack(pady=20)

color_array = []

def drawbars(data):
    c_height = 320
    c_width = 650
    margin = 20
    bar_width = (c_width - 2 * margin) / len(data)
    max_value = max(data)

    canvas.delete("all")
    for i, val in enumerate(data):
        x0 = margin + i * bar_width
        y0 = c_height - (val / max_value) * (c_height - 40)
        x1 = margin + (i + 1) * bar_width
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text((x0 + x1) / 2, y0, anchor=S, text=str(val), fill="black")

    root.update()

def insertionsort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1

        color_array[i] = "red" 
        drawbars(data)
        time.sleep(0.3)

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            color_array[j] = "yellow"  
            drawbars(data)
            time.sleep(0.3)
            color_array[j] = "blue"
            j -= 1

        data[j + 1] = key


        color_array[j + 1] = "green"
        drawbars(data)
        time.sleep(0.3)

    for k in range(n):
        color_array[k] = "green"
    drawbars(data)


def take_input():
    global user_data, color_array
    user_input = simpledialog.askstring("Input", "Enter numbers separated by commas:")
    if user_input:
        user_data = list(map(int, user_input.split(",")))
        color_array = ["blue"] * len(user_data)
        drawbars(user_data)


def start_sort():
    insertionsort(user_data)


Button(root, text="Enter Array", command=take_input, font=("Arial", 14)).pack(pady=10)
Button(root, text="Start Sorting", command=start_sort, font=("Arial", 14)).pack()

root.mainloop()
