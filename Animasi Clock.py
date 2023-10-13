import tkinter as tk
import time
import math

# Fungsi untuk menggambar jarum jam
def draw_clock():
    canvas.delete("all")
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour

    # Menghitung sudut untuk jarum detik, menit, dan jam
    sec_angle = math.radians(6 * seconds)
    min_angle = math.radians(6 * minutes + 0.1 * seconds)
    hour_angle = math.radians(30 * hours + 0.5 * minutes)

    # Menggambar lingkaran jam
    canvas.create_oval(10, 10, 190, 190, width=2)
    
    # Menggambar jarum detik
    sec_x = 100 + 40 * math.sin(sec_angle)
    sec_y = 100 - 40 * math.cos(sec_angle)
    canvas.create_line(100, 100, sec_x, sec_y, width=1, fill='red')

    # Menggambar jarum menit
    min_x = 100 + 35 * math.sin(min_angle)
    min_y = 100 - 35 * math.cos(min_angle)
    canvas.create_line(100, 100, min_x, min_y, width=3, fill='blue')

    # Menggambar jarum jam
    hour_x = 100 + 30 * math.sin(hour_angle)
    hour_y = 100 - 30 * math.cos(hour_angle)
    canvas.create_line(100, 100, hour_x, hour_y, width=4, fill='black')
    
    # Menggambar tengah jam
    canvas.create_oval(95, 95, 105, 105, fill='black')

    # Memanggil fungsi draw_clock setiap 1000 ms (1 detik)
    root.after(1000, draw_clock)

# Membuat jendela aplikasi
root = tk.Tk()
root.title("Jam Analog")

# Membuat elemen canvas untuk menggambar jam
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Memanggil fungsi untuk menggambar jam
draw_clock()

# Menjalankan aplikasi
root.mainloop()
