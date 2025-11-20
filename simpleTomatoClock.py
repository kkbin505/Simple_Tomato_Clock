import tkinter as tk
from tkinter import messagebox

# --- Parameter ---
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
CYCLES = 4

# --- Global Variable ---
reps = 0            
timer = None        
is_running = False  

# --- Function ---

def start_timer():
    """Caculate the reps will triger different rest time"""
    global reps, is_running
    
    if is_running:
        return 
        
    reps += 1
    is_running = True

    # Color Font
    if reps % (CYCLES * 2) == 0:
        count_sec = LONG_BREAK_MIN * 60
        status_text = "Long Rest" # 
        window_bg = "#ad084d" 
        messagebox.showinfo(title="Tomato Clock", message="Long Rest！")
    elif reps % 2 == 0:
        count_sec = SHORT_BREAK_MIN * 60
        status_text = "Shot Rest" # 
        window_bg = "#568203" 
        messagebox.showinfo(title="Tomato Clock", message="5 min rest！")
    else:
        count_sec = WORK_MIN * 60
        status_text = "Focus" # 
        window_bg = "#ffffff" 
        
    # Update GUI
    window.config(bg=window_bg)
    tomato_canvas.config(bg=window_bg)
    timer_label.config(bg=window_bg)
    
    status_label.config(bg=window_bg, text=status_text)
    
    countdown(count_sec)

def countdown(count):
    """Count"""
    global timer, is_running
    
    minutes = count // 60
    seconds = count % 60
    time_format = f"{minutes:02d}:00"
    
    timer_label.config(text=time_format) 
    
    if count > 0:
        timer = window.after(60000, countdown, count - 60)
    else:
        is_running = False
        start_timer()


def reset_timer():
    """Rest"""
    global reps, is_running, timer
    if timer:
        window.after_cancel(timer) 
    reps = 0
    is_running = False
    
    # 
    window.config(bg="white")
    tomato_canvas.config(bg="white")
    timer_label.config(bg="white", text="00:00")
    status_label.config(bg="white", text="") 
    
# --- GUI  ---

window = tk.Tk()
window.title("Tomato Clock") 

# 
window.config(padx=2, pady=2, bg="white")
window.wm_attributes("-topmost", 1) # Top most window

# --- Column 0：Draw mini tomato ---
# 💥 ：40x40 Canvas
tomato_canvas = tk.Canvas(width=40, height=40, bg="white", highlightthickness=0)

tomato_canvas.create_rectangle(19, 3, 21, 10, fill="green3", outline="green3") 
tomato_canvas.create_oval(10, 8, 30, 35, fill="red", outline="red") 

tomato_canvas.grid(row=0, column=0, padx=2) 

# --- Column 1：Clock ---
# 💥 Font (20)
timer_label = tk.Label(window, text="00:00", bg="white", font=("Courier", 20, "bold"))
timer_label.grid(row=0, column=1, padx=5) 

# --- Column 2：Status ---
status_label = tk.Label(window, text="", fg="black", bg="white", font=("Courier", 8))
status_label.grid(row=0, column=2, padx=2) 

# --- Column 3：Start Button ---
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer, font=("", 10))
start_button.grid(row=0, column=3, padx=1, pady=1) 

# --- Column 4：Reset ---
reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer, font=("", 10))
reset_button.grid(row=0, column=4, padx=1, pady=1) 

window.grid_rowconfigure(0, weight=1)

window.mainloop()