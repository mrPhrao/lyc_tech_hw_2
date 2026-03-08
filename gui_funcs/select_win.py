from python.tkinter.project.gui_funcs.general import *
from tkinter import Toplevel
from tkinter import messagebox
from python.tkinter.project.colors import *


def on_confirm(window):
    window.destroy()


def after_confirm(var1, var2, var3, var4, var5, var6, var7, var8, data):
    if data is None:
        print(f"LOG : got no data")
        return

    parts = data.split('/')
    lon, lat = parts

    show_wanted_data(city='', var1=var1, var2=var2, var3=var3,
                     var4=var4, var5=var5, var6=var6, var7=var7, var8=var8,
                     lat=float(lat), lon=float(lon))


def show_city_selection(city_name, callback):
    selection_window = Toplevel()
    selection_window.title("Select Location")
    selection_window.geometry("500x500+650+200")
    selection_window.transient()
    selection_window.grab_set()
    selection_window.resizable(False, False)
    selection_window.configure(bg=light_gray_frame)

    cords = tk.Variable()
    cords.set(None)

    def on_cancel():
        selection_window.destroy()
        callback(None)

    def on_confirm():
        if cords.get():
            callback(cords.get())
            selection_window.destroy()
        else:
            messagebox.showwarning(title='Warning', message='Please select a location')

    header_frame = tk.Frame(selection_window, bg=primary_blue, height=80)
    header_frame.pack(fill='x')
    header_frame.pack_propagate(False)

    tk.Label(
        header_frame,
        text="Select Location",
        font=("Arial", 20, "bold"),
        bg=primary_blue,
        fg=white_text
    ).pack(expand=True)

    tk.Label(
        header_frame,
        text=f"for: {city_name.title()}",
        font=("Arial", 12),
        bg=primary_blue,
        fg=white_text
    ).pack(expand=True)

    radio_frame = tk.Frame(selection_window, bg=white, relief='groove', bd=2)
    radio_frame.pack(fill='both', expand=True, padx=20, pady=15)

    locations = get_all_locations(city_name)

    if not locations:
        tk.Label(
            radio_frame,
            text="❌ No locations found",
            font=("Arial", 14),
            bg=white,
            fg=error_red
        ).pack(pady=30)
    else:
        inner_frame = tk.Frame(radio_frame, bg=white)
        inner_frame.pack(fill='both', expand=True, padx=10, pady=10)

        for i, loc in enumerate(locations):
            country = loc['country']
            state = loc.get('state', '')
            name = loc.get('city', city_name)

            if state:
                display_text = f"{name}, {state}, {country}"
            else:
                display_text = f"{name}, {country}"

            bg_color = off_white if i % 2 == 0 else white

            rb = tk.Radiobutton(
                inner_frame,
                text=display_text,
                variable=cords,
                value=f"{loc['lon']}/{loc['lat']}",
                font=("Arial", 11),
                bg=bg_color,
                anchor='w',
                selectcolor=white,
                padx=10
            )
            rb.pack(fill='x', pady=2)

    button_frame = tk.Frame(selection_window, bg=light_gray_frame, height=70)
    button_frame.pack(fill='x', side='bottom')
    button_frame.pack_propagate(False)

    confirm_btn = tk.Button(
        button_frame,
        text='Confirm',
        command=on_confirm,
        font=("Arial", 12, "bold"),
        bg=success_green,
        fg=white_text,
        width=12,
        cursor='hand2'
    )
    confirm_btn.pack(side='right', padx=15, pady=15)

    cancel_btn = tk.Button(
        button_frame,
        text='Cancel',
        command=on_cancel,
        font=("Arial", 12, "bold"),
        bg=error_red,
        fg=white_text,
        width=12,
        cursor='hand2'
    )
    cancel_btn.pack(side='right', padx=5, pady=15)

    tk.Label(
        button_frame,
        text=f"Found {len(locations)} location(s)",
        font=("Arial", 9, "italic"),
        bg=light_gray_frame,
        fg=medium_gray_text
    ).pack(side='left', padx=15, pady=15)
