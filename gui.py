import tkinter as tk
from moon import Moon


def send_command():

    phobos = Moon(int(input_phobos_rise_hour.get()),int(input_phobos_rise_minute.get()),int(input_phobos_set_hour.get()),int(input_phobos_set_minute.get()),'Phobos')
    deimos = Moon(int(input_deimos_rise_hour.get()),int(input_deimos_rise_minute.get()),int(input_deimos_set_hour.get()),int(input_deimos_set_minute.get()),'Deimos')
    overlap = phobos.calculate_overlap_time(deimos)
    return_label.config(text="Overlaping time: " + str(overlap) + " min")

def check_hour(value):
    try: 
        value_integer = int(value.strip() or 0)
    except ValueError:
        return False
    return (0 <= int(value_integer) and int(value_integer) <= 24) and len(value)<=2

def check_minute(value):
    try: 
        value_integer = int(value.strip() or 0)
    except ValueError:
        return False
    return (0 <= int(value_integer) and int(value_integer) <= 99) and len(value)<=2

# Ein Fenster erstellen
window = tk.Tk()
window.title("MARS")
validation_hour = window.register(check_hour)
validation_minute = window.register(check_minute)

label_colon1 = tk.Label(window,text=":")
label_colon2 = tk.Label(window,text=":")
label_colon3 = tk.Label(window,text=":")
label_colon4 = tk.Label(window,text=":")

label_phobos_rise = tk.Label(window,text="Phobos rise")
input_phobos_rise_hour = tk.Entry(window, validate="key", validatecommand=(validation_hour,'%P'))
input_phobos_rise_minute = tk.Entry(window, validate="key", validatecommand=(validation_minute,'%P'))

label_phobos_set = tk.Label(window,text="Phobos set")
input_phobos_set_hour = tk.Entry(window, validate="key", validatecommand=(validation_hour,'%P'))
input_phobos_set_minute = tk.Entry(window, validate="key", validatecommand=(validation_minute,'%P'))

label_deimos_rise = tk.Label(window,text="Deimos rise")
input_deimos_rise_hour = tk.Entry(window, validate="key", validatecommand=(validation_hour,'%P'))
input_deimos_rise_minute = tk.Entry(window, validate="key", validatecommand=(validation_minute,'%P'))

label_deimos_set = tk.Label(window,text="Deimos set")
input_deimos_set_hour = tk.Entry(window, validate="key", validatecommand=(validation_hour,'%P'))
input_deimos_set_minute = tk.Entry(window, validate="key", validatecommand=(validation_minute,'%P'))

label_phobos_rise.grid(row=0, column=0) 
input_phobos_rise_hour.grid(row=0, column=1) 
label_colon1.grid(row=0, column=2) 
input_phobos_rise_minute.grid(row=0, column=3) 
label_phobos_set.grid(row=0, column=4) 
input_phobos_set_hour.grid(row=0, column=5) 
label_colon2.grid(row=0, column=6) 
input_phobos_set_minute.grid(row=0, column=7) 

label_deimos_rise.grid(row=1, column=0) 
input_deimos_rise_hour.grid(row=1, column=1)
label_colon3.grid(row=1, column=2) 
input_deimos_rise_minute.grid(row=1, column=3)
label_deimos_set.grid(row=1, column=4) 
input_deimos_set_hour.grid(row=1, column=5)
label_colon4.grid(row=1, column=6) 
input_deimos_set_minute.grid(row=1, column=7)

send_button = tk.Button(window,text="Calculate overlap",command=send_command)
send_button.grid(row=2,column=0)
return_label = tk.Label(window,text="")
return_label.grid(row=2,column=1)

window.mainloop()