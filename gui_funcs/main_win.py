from python.tkinter.project.gui_funcs.select_win import *
from python.tkinter.project.gui_funcs.general import *


def show_instruction():
    message = '''Input city in entry field\nChoose information you want to see.\nPress "Get Weather" to see result.\n
If there are multiple cities with entered name, you will have to choose one of them'''
    messagebox.showinfo(title='Instruction', message=message)


def on_focusout(city):
    if city.get() == '':
        city.insert(0, 'Enter city name...')
        city.config(fg=medium_gray_text)


def on_focusin(city):
    if city.get() == 'Enter city name...' and city.cget('fg') == medium_gray_text:
        city.delete(0, tk.END)
        city.config(fg='black')


def main_confirm(city, var1, var2, var3, var4, var5, var6, var7, var8):
    error = validate_city(city)
    city_name = city.get()

    if error == '':
        countries = get_all_locations(city_name)
        if len(countries) == 1:
            show_wanted_data(city_name, var1, var2, var3, var4, var5, var6, var7, var8, lat='', lon='')
        else:
            def callback(data):
                after_confirm(var1, var2, var3, var4, var5, var6, var7, var8, data)

            show_city_selection(city_name, callback)

    if error == 'existence_error':
        message = f"Such city : {city_name} doesn't exist"
        messagebox.showerror(title='Error', message=message)
    if error == 'input_error':
        message = f"Invalid name.\nCity name can only contain english letters"
        messagebox.showerror(title='Error', message=message)
    if error == 'empty_error':
        message = f"City must not be empty"
        messagebox.showerror(title='Error', message=message)
