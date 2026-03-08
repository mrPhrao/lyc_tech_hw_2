from python.tkinter.project.gui_funcs.main_win import *
from python.tkinter.project.colors import *

root = tk.Tk()
root.geometry('600x700+650+100')
root.resizable(False, False)
root.title('Weather Data App')

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()
var5 = tk.BooleanVar()
var6 = tk.BooleanVar()
var7 = tk.BooleanVar()
var8 = tk.BooleanVar()

check_font = ('Arial', 11)
mini_font = ("Arial", 18, "bold")

header_frame = tk.LabelFrame(root, bg=primary_blue, height=60)
header_frame.pack(fill='x', anchor='center')
header_frame.pack_propagate(False)

tk.Label(
    header_frame,
    text="Weather Information App",
    font=("Arial", 18, "bold"),
    bg=primary_blue,
    fg=white
).pack(expand=True, anchor='center')

city_frame = tk.LabelFrame(root,
                           font=('Arial', 12, 'bold'),
                           text='City Selection',
                           padx=10, pady=10)
city_frame.pack(fill='x', padx=20, pady=10)

city = tk.Entry(city_frame, width=30, font=('arial', 12))
city.pack(fill='x', padx=10, pady=5)

city.insert(0, 'Enter city name...')
city.config(fg=medium_gray_text)
city.bind('<FocusIn>', lambda event: on_focusin(city))
city.bind('<FocusOut>', lambda event: on_focusout(city))

select_frame = tk.LabelFrame(root, text="Weather Parameters", font=mini_font, padx=10, pady=10)
select_frame.pack(fill='both', expand=True, padx=20, pady=10)

inner_select = tk.Frame(select_frame)
inner_select.pack(fill='both', expand=True, padx=10, pady=10)

inner_select.columnconfigure(0, weight=1, uniform='col')
inner_select.columnconfigure(1, uniform='col')

tk.Checkbutton(inner_select,
               text='Temperature',
               variable=var1,
               font=check_font,
               anchor='w',
               cursor='hand2',
               padx=5, pady=3,
               selectcolor=white).grid(row=0, column=0, sticky='w', padx=10, pady=2)

tk.Checkbutton(inner_select,
               text='Min/Max Temp',
               variable=var2,
               font=check_font,
               anchor='w',
               cursor='hand2',
               padx=5, pady=3,
               selectcolor=white).grid(row=1, column=0, sticky='w', padx=10, pady=2)

tk.Checkbutton(inner_select,
               text='Humidity',
               variable=var3,
               font=check_font,
               anchor='w',
               cursor='hand2',
               padx=5, pady=3,
               selectcolor=white).grid(row=2, column=0, sticky='w', padx=10, pady=2)

tk.Checkbutton(inner_select,
               text='Pressure',
               variable=var4,
               font=check_font,
               anchor='w',
               cursor='hand2',
               padx=5, pady=3,
               selectcolor=white).grid(row=3, column=0, sticky='w', padx=10, pady=2)

tk.Checkbutton(inner_select,
               text='Wind Data',
               variable=var5,
               font=check_font,
               anchor='w',
               cursor='hand2',
               padx=5, pady=3,
               selectcolor=white).grid(row=0, column=1, sticky='w', padx=10, pady=2)

tk.Checkbutton(inner_select,
               text='Clouds Data',
               variable=var6,
               font=check_font,
               anchor='w',
               cursor='hand2',
               padx=5, pady=3,
               selectcolor=white).grid(row=1, column=1, sticky='w', padx=10, pady=2)

tk.Checkbutton(inner_select,
               text='Visibility',
               variable=var7,
               font=check_font,
               anchor='w',
               cursor='hand2',
               padx=5, pady=3,
               selectcolor=white).grid(row=2, column=1, sticky='w', padx=10, pady=2)

tk.Checkbutton(inner_select,
               text='Timezone',
               variable=var8,
               font=check_font,
               anchor='w',
               cursor='hand2',
               padx=5, pady=3,
               selectcolor=white).grid(row=3, column=1, sticky='w', padx=10, pady=2)


button_frame = tk.Frame(root)
button_frame.pack(fill='x', padx=20, pady=15)

confirm = tk.Button(
    button_frame,
    text='Get Weather',
    command=lambda: main_confirm(city, var1, var2, var3, var4, var5, var6, var7, var8),
    bg=success_green,
    fg=white,
    font=mini_font,
    width=15,
    height=2,
    cursor='hand2'
)
confirm.pack(side='left', padx=5, expand=True, fill='x')

instruction = tk.Button(
    button_frame,
    text='Instructions',
    command=show_instruction,
    bg=primary_blue,
    fg=white,
    font=mini_font,
    width=15,
    height=2,
    cursor='hand2'
)
instruction.pack(side='left', padx=5, expand=True, fill='x')

root.mainloop()
