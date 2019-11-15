from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import commands

def show_error():
    for widget in root_graph.winfo_children():
        widget.destroy()

    for widget in root_error.winfo_children():
        widget.destroy()

    label1 = Label(root_graph, text="Unsupported input values", font='arial 50')
    label2 = Label(root_error, text="Unsupported input values", font='arial 30')

    label1.pack()
    label2.pack()


def press_draw(event):
    for widget in root_graph.winfo_children():
        widget.destroy()

    for widget in root_error.winfo_children():
        widget.destroy()

    fig1 = Figure(figsize=(5, 4), dpi=100)
    fig2 = Figure(figsize=(5, 4), dpi=100)
    fig3 = Figure(figsize=(5, 4), dpi=100)

    my_x0 = float(x_entry.get())
    my_y0 = float(y_entry.get())
    my_X = float(X_entry.get())
    my_N = int(N_entry.get())

    if my_x0 < 0 < my_X or my_N < 2:
        show_error()
        return 0

    rows_number = 0
    for i in range(len(method_vars)):
        rows_number += method_vars[i].get()

    if rows_number != 0:
        for i in range(len(method_vars)):
            if method_vars[i].get() == 1:
                if method_list_names[i] == "Exact solution":
                    #todo exact
                    exact_result = commands.calculate(my_x0, my_y0, my_X, my_N)
                    fig1.add_subplot(111).plot(exact_result['xs'], exact_result['ys'], label=method_list_names[i])
                    fig2.add_subplot(111).plot(exact_result['xs'], exact_result['error'], label=method_list_names[i]+' error')
                    fig3.add_subplot(111).plot(exact_result['xs'], exact_result['total_error'], label=method_list_names[i]+' total error')
                elif method_list_names[i] == "Euler's method":
                    #todo euler
                    euler_result = commands.calculate_euler(my_x0, my_y0, my_X, my_N)
                    fig1.add_subplot(111).plot(euler_result['xs'], euler_result['ys'], label=method_list_names[i])
                    fig2.add_subplot(111).plot(euler_result['xs'], euler_result['error'],
                                               label=method_list_names[i] + ' error')
                    fig3.add_subplot(111).plot(euler_result['xs'], euler_result['total_error'],
                                               label=method_list_names[i] + ' total error')
                elif method_list_names[i] == "improved Euler’s method":
                    #todo euler impr
                    euler_imp_result = commands.calculate_imp_euler(my_x0, my_y0, my_X, my_N)
                    fig1.add_subplot(111).plot(euler_imp_result['xs'], euler_imp_result['ys'], label=method_list_names[i])
                    fig2.add_subplot(111).plot(euler_imp_result['xs'], euler_imp_result['error'],
                                               label=method_list_names[i] + ' error')
                    fig3.add_subplot(111).plot(euler_imp_result['xs'], euler_imp_result['total_error'],
                                               label=method_list_names[i] + ' total error')
                elif method_list_names[i] == "Runge-Kutta method":
                    #todo runge
                    runge_result = commands.calculate_runge(my_x0, my_y0, my_X, my_N)
                    fig1.add_subplot(111).plot(runge_result['xs'], runge_result['ys'], label=method_list_names[i])
                    fig2.add_subplot(111).plot(runge_result['xs'], runge_result['error'],
                                               label=method_list_names[i] + ' error')
                    fig3.add_subplot(111).plot(runge_result['xs'], runge_result['total_error'],
                                               label=method_list_names[i] + ' total error')

        fig1.legend(loc='upper center')
        fig2.legend(loc='upper center')
        fig3.legend(loc='upper center')

    canvas1 = FigureCanvasTkAgg(fig1, master=root_graph)
    canvas1.draw()
    canvas1.get_tk_widget().pack()

    if params_vars[1].get():
        canvas2 = FigureCanvasTkAgg(fig2, master=root_graph)
        canvas2.draw()
        canvas2.get_tk_widget().pack()

    if params_vars[0].get():
        canvas3 = FigureCanvasTkAgg(fig3, master=root_error)
        canvas3.draw()
        canvas3.get_tk_widget().pack()


root_settings = Tk()
root_graph = Tk()
root_error = Tk()

root_settings.title('Graph settings')
root_settings.geometry('500x377+0+0')
root_settings.resizable(False, False)

eq_photo = PhotoImage(file="equation.png").subsample(2)
eq_but_photo = Button(root_settings, image=eq_photo)
eq_but_photo.grid(row=0, column=0, columnspan=2)

label_x = Label(root_settings, text='x0', font='arial 15')
label_x.grid(row=1, column=0)

x_entry = Entry(root_settings, text='x0', font='arial 15', )
x_entry.insert(0, commands.main_x)
x_entry.grid(row=1, column=1)

label_y = Label(root_settings, text='y0', font='arial 15')
label_y.grid(row=2, column=0)

y_entry = Entry(root_settings, text='y0', font='arial 15', )
y_entry.insert(0, commands.main_y)
y_entry.grid(row=2, column=1)

label_X = Label(root_settings, text='X', font='arial 15')
label_X.grid(row=3, column=0)

X_entry = Entry(root_settings, text='X', font='arial 15', )
X_entry.insert(0, commands.main_upper_x)
X_entry.grid(row=3, column=1)

label_N = Label(root_settings, text='N', font='arial 15')
label_N.grid(row=4, column=0)

N_entry = Entry(root_settings, text='N', font='arial 15', )
N_entry.insert(0, commands.main_N)
N_entry.grid(row=4, column=1)

draw_button = Button(root_settings, text='Draw', font='arial 20')
draw_button.bind("<Button-1>", press_draw)
draw_button.grid(row=8, column=3)

method_list_names = ["Exact solution", "Euler's method", "improved Euler’s method", "Runge-Kutta method"]
method_vars = [IntVar() for name in method_list_names]
method_list = [Checkbutton(root_settings,
                           text=method_list_names[i],
                           variable=method_vars[i],
                           onvalue=1,
                           offvalue=0).grid(row=5 + i, column=0) for i in range(len(method_list_names))]

params_list_names = ["Total approximation error", "Local error"]
params_vars = [IntVar() for p_name in params_list_names]
params_list = [Checkbutton(root_settings,
                           text=params_list_names[i],
                           variable=params_vars[i],
                           onvalue=1,
                           offvalue=0).grid(row = 5 + i, column=1) for i in range(len(params_list_names))]

root_graph.title('Graph')
root_graph.geometry("{}x{}+{}+{}".format(700, 700, 500, 0))
root_graph.resizable(False, False)

root_error.title('Total error')
root_error.geometry("{}x{}+{}+{}".format(500,300,0,400))
root_error.resizable(False, False)

root_error.after(300, root_error.mainloop)
root_graph.after(500, root_graph.mainloop)
root_settings.mainloop()
