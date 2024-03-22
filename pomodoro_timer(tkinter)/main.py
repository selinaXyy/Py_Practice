from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = '\u2714'
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    lbl_timer["text"] = "Timer"
    lbl_checkmark["text"] = ""

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        lbl_timer.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        lbl_timer.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        lbl_timer.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count_in_sec):
    current_min = int(count_in_sec / 60)
    current_sec = count_in_sec % 60
    if current_sec < 10:
        current_sec = f"0{current_sec}"

    canvas.itemconfig(timer_text, text=f"{current_min}:{current_sec}")
    if count_in_sec > 0:
        global timer
        timer = window.after(1000, count_down, count_in_sec-1)
    else:
        start_timer()
        records = ""
        work_sessions = int(reps / 2)
        for _ in range(work_sessions):
            records += check_mark + " "
        lbl_checkmark["text"] = records

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

#label
lbl_timer = Label(text="Timer",fg=GREEN, font=(FONT_NAME, 45, "normal"), bg=YELLOW)
lbl_timer.grid(row=0, column=1)

lbl_checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
lbl_checkmark.grid(row=3, column=1)

#canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#button
btn_start = Button(text="Start", padx=0, pady=0, borderwidth=0, command=start_timer)
btn_start.grid(row=2, column=0)

btn_reset = Button(text="Reset", padx=0, pady=0,borderwidth=0, command=reset_timer)
btn_reset.grid(row=2, column=2)

window.mainloop()