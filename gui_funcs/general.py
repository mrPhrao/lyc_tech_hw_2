from python.tkinter.project.api.api import *
from python.tkinter.project.colors import *
import tkinter as tk
import re


def get_wanted_types(var1, var2, var3, var4, var5, var6, var7, var8):
    wanted = ['general', 'description']

    if var1.get():
        wanted.append('temperature')
        wanted.append('feels_like')
    if var2.get():
        wanted.append('temp_min')
        wanted.append('temp_max')
    if var3.get():
        wanted.append('humidity')
    if var4.get():
        wanted.append('pressure')
    if var5.get():
        wanted.append('wind_speed')
        wanted.append('wind_dir')
        wanted.append('gust')
    if var6.get():
        wanted.append('clouds')
    if var7.get():
        wanted.append('visibility')
    if var8.get():
        wanted.append('timezone')

    return wanted


def validate_city(entry):
    city = str(entry.get())
    error = ''

    if city == '' or city == 'Enter city name...':
        error = 'empty_error'
    elif not bool(re.match(r'^[a-zA-Z\s]+$', city)):
        error = 'input_error'
    elif not check_city_exists(city):
        error = 'existence_error'

    return error


def show_wanted_data(city, var1, var2, var3, var4, var5, var6, var7, var8, lat, lon):
    if city == '' and lat and lon:
        data = get_all_cords_info(float(lat), float(lon))
    else:
        data = get_all_city_info(city)

    result_window = tk.Toplevel()
    result_window.title(f"Weather in {data['city']}, {data['country']}")
    result_window.geometry("450x500")
    result_window.transient()
    result_window.grab_set()
    result_window.resizable(False, False)

    header = tk.Frame(result_window, bg=primary_blue, height=50)
    header.pack(fill='x')
    header.pack_propagate(False)

    tk.Label(
        header,
        text=f"{data['city']}, {data['country']}",
        font=("Arial", 16, "bold"),
        bg=primary_blue,
        fg=white
    ).pack(expand=True)

    main_info = tk.Frame(result_window, bg=very_light_blue, height=80)
    main_info.pack(fill='x')
    main_info.pack_propagate(False)

    tk.Label(
        main_info,
        text=f"General Data : {data['general']} - {data['description']}",
        font=("Arial", 14),
        bg=very_light_blue
    ).pack(expand=True)

    details_frame = tk.Frame(result_window)
    details_frame.pack(fill='both', expand=True, padx=15, pady=10)

    wanted_info = get_wanted_types(var1, var2, var3, var4, var5, var6, var7, var8)

    row = 0
    for key in wanted_info:
        if key in data and key not in ['general', 'description']:
            display_name = key.replace('_', ' ').title()

            row_frame = tk.Frame(details_frame, bg=white if row % 2 == 0 else light_gray_bg)
            row_frame.pack(fill='x', pady=1)

            tk.Label(
                row_frame,
                text=f"{display_name}:",
                font=('Arial', 11, 'bold'),
                bg=row_frame['bg'],
                width=15,
                anchor='w'
            ).pack(side='left', padx=10, pady=5)

            tk.Label(
                row_frame,
                text=data[key],
                font=('arial', 11),
                bg=row_frame['bg'],
                anchor='w'
            ).pack(side='left', padx=5, pady=5)

            row += 1
