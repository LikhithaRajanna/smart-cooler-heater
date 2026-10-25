import tkinter as tk
from tkinter import messagebox
import serial
import time

# ============================================================
# SERIAL CONFIGURATION
# ============================================================

try:
    ser = serial.Serial(
        'COM3',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    time.sleep(1)
    serial_connected = True

except Exception as e:
    ser = None
    serial_connected = False
    print("Serial Error:", e)


# ============================================================
# SEND DATA
# ============================================================

def Send(data):
    if ser is not None and ser.is_open:
        ser.write(data.encode())
        print("Data sent:", data)

        status_label.config(
            text=f"Command Sent: {data}"
        )
    else:
        messagebox.showerror(
            "Serial Error",
            "Serial port COM40 is not connected."
        )


# ============================================================
# BUTTON FUNCTIONS
# ============================================================

def heater_level1():
    Send("A")


def heater_level2():
    Send("B")


def cooler():
    Send("C")


def stop():
    Send("D")


# ============================================================
# CLOSE PROGRAM
# ============================================================

def close_program():
    if ser is not None and ser.is_open:
        ser.close()

    root.destroy()


# ============================================================
# TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title("Air Cooler & Heater Control")
root.geometry("500x450")
root.resizable(False, False)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="AIR COOLER & HEATER CONTROL",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=25)


# ============================================================
# BUTTON FRAME
# ============================================================

button_frame = tk.Frame(root)
button_frame.pack(pady=10)


# ============================================================
# HEATER LEVEL 1
# ============================================================

btn_heater1 = tk.Button(
    button_frame,
    text="HEATER LEVEL 1",
    command=heater_level1,
    font=("Arial", 14, "bold"),
    width=25,
    height=2
)

btn_heater1.pack(pady=8)


# ============================================================
# HEATER LEVEL 2
# ============================================================

btn_heater2 = tk.Button(
    button_frame,
    text="HEATER LEVEL 2",
    command=heater_level2,
    font=("Arial", 14, "bold"),
    width=25,
    height=2
)

btn_heater2.pack(pady=8)


# ============================================================
# COOLER
# ============================================================

btn_cooler = tk.Button(
    button_frame,
    text="COOLER",
    command=cooler,
    font=("Arial", 14, "bold"),
    width=25,
    height=2
)

btn_cooler.pack(pady=8)


# ============================================================
# STOP
# ============================================================

btn_stop = tk.Button(
    button_frame,
    text="STOP",
    command=stop,
    font=("Arial", 14, "bold"),
    width=25,
    height=2
)

btn_stop.pack(pady=8)


# ============================================================
# STATUS
# ============================================================

status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 12)
)

status_label.pack(pady=20)


# ============================================================
# CLOSE EVENT
# ============================================================

root.protocol("WM_DELETE_WINDOW", close_program)


# ============================================================
# START GUI
# ============================================================

root.mainloop()
