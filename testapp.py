import tkinter as tk
import time

def clock_start():
    global clock_label
    clock_label = tk.Label(main, font=('Arial', 20))
    clock_label.place(x=150, y=50)
    update_clock()

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    main.after(1000, update_clock)  # Обновление времени каждую секунду

def clock_stop():
    if 'clock_label' in globals():
        clock_label.destroy()



        
def start_stopwatch():
    global running
    running = True
    global start_time
    start_time = time.time() - elapsed_time
    update()

def stop_stopwatch():
    global running
    running = False

def reset_stopwatch():
    global elapsed_time
    global running
    running = False
    elapsed_time = 0
    label.config(text="00:00:00")

def update():
    global running
    if running:
        global start_time
        global elapsed_time
        elapsed_time = time.time() - start_time
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 100)
        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
        label.config(text=time_string)
        label.after(1, update)


main = tk.Tk()
main.title('MainWindow')
main.geometry('1600x900')

elapsed_time = 0
running = False

label = tk.Label(main, text="00:00:00", font=("Arial", 30))
label.pack(padx=10, pady=10)

start_button = tk.Button(main, text="Start", command=start_stopwatch)
start_button.place(x=650, y=100)

stop_button = tk.Button(main, text="Stop", command=stop_stopwatch)
stop_button.place(x=730, y=100)

reset_button = tk.Button(main, text="Reset", command=reset_stopwatch)
reset_button.place(x=800, y=100)
    
button_start = tk.Button(main, text='Clock start', command=clock_start)
button_start.place(x=100, y=100)

button_stop = tk.Button(main, text='Stop clock', command=clock_stop)
button_stop.place(x=200, y=100)

entry = tk.Entry(main)
entry.pack()
    
main.mainloop()