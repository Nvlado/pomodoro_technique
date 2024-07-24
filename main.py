from tkinter import *
from PIL import Image, ImageTk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short break")
    else:
        count_down(70)
        label.config(text="Work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
input_image_path = "pngegg.png"
original_image = Image.open(input_image_path)
window.config(padx=100, pady=100, bg="yellow")

label = Label(text="Timer", bg="yellow", padx=10, font=("Arial", 35))
label.grid(column=1, row=0)

target_width = 300
width_percent = (target_width / float(original_image.size[0]))
target_height = int((float(original_image.size[1]) * float(width_percent)))
resized_image = original_image.resize((target_width, target_height))
img = ImageTk.PhotoImage(resized_image)
canvas = Canvas(window, width=400, height=400, bg="yellow", highlightthickness=0)
canvas.create_image(50, 0, anchor='nw', image=img)
timer_text = canvas.create_text(210, 240, text="00:00", font=("Arial", 35, "normal"), fill="white")
canvas.grid(column=1, row=1, padx=100, pady=0)


start_button = Button(text="Start", command=start_timer, font=("Arial", 20))
start_button.grid(column=0, row=3)

check_mark = Label(font=("Arial", 35), bg="yellow")
check_mark.grid(column=1, row=2)

reset_button = Button(text="Reset", command=reset_timer, font=("Arial", 20))
reset_button.grid(column=2, row=3)

window.mainloop()
