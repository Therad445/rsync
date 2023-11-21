# tkinter_app.py
import tkinter.messagebox as mb

from tkinter import *
from tkinter import filedialog
from rsync import Rsync
import ipaddress


class RsyncGUI:
    def __init__(self, master):
        self.save_button = None
        self.port_entry = None
        self.port_label = None
        self.ip_entry = None
        self.ip_label = None
        self.user_entry = None
        self.user_label = None
        self.master = master
        master.title("Rsync GUI")
        self.code = StringVar()
        self.code.set(NONE)

        self.source_label = Label(master, text="Source:")
        self.source_label.grid(row=0, column=0)

        self.source_entry = Entry(master, width=50)
        self.source_entry.grid(row=0, column=1)

        self.source_button = Button(master, text="Browse", command=self.browse_source)
        self.source_button.grid(row=0, column=2)

        self.dest_label = Label(master, text="Destination:")
        self.dest_label.grid(row=1, column=0)

        self.dest_entry = Entry(master, width=50)
        self.dest_entry.grid(row=1, column=1)

        self.dest_button = Button(master, text="Browse", command=self.browse_dest)
        self.dest_button.grid(row=1, column=2)

        self.copy_button = Button(master, text="Copy", command=self.copy)
        self.copy_button.grid(row=2, column=1)

        self.setting = Button(master, text="Setting server", command=self.setting_server)
        self.setting.grid(row=3, column=1)

        self.local_radio = Radiobutton(master, text="Local copy", value="-azvh", variable=self.code)
        self.local_radio.grid(row=2, column=0)

        self.remote_radio = Radiobutton(master, text="Remote copy", value="-avz", variable=self.code)
        self.remote_radio.grid(row=2, column=2)

    def browse_source(self):
        source_dir = filedialog.askdirectory()
        self.source_entry.delete(0, END)
        self.source_entry.insert(0, source_dir)

    def browse_dest(self):
        dest_dir = filedialog.askdirectory()
        self.dest_entry.delete(0, END)
        self.dest_entry.insert(0, dest_dir)

    def copy(self):
        if len(self.source_entry.get()) == 0 and len(self.dest_entry.get()) == 0:
            self.show_error_copy()
            return
        code = self.code.get()
        source_dir = self.source_entry.get()
        dest_dir = self.dest_entry.get()
        rsync = Rsync(code, source_dir, dest_dir)
        rsync.run()
        self.success_info()

    def setting_server(self):
        new_window_1 = Toplevel()
        # self.master = second_master
        new_window_1.title("Setting server Rsync GUI")

        self.user_label = Label(new_window_1, text="User:")
        self.user_label.grid(row=0, column=0)

        self.user_entry = Entry(new_window_1, width=50)
        self.user_entry.grid(row=0, column=1)

        self.ip_label = Label(new_window_1, text="Ip:")
        self.ip_label.grid(row=1, column=0)

        self.ip_entry = Entry(new_window_1, width=50)
        self.ip_entry.grid(row=1, column=1)

        self.port_label = Label(new_window_1, text="Port:")
        self.port_label.grid(row=2, column=0)

        self.port_entry = Entry(new_window_1, width=50)
        self.port_entry.grid(row=2, column=1)

        self.save_button = Button(new_window_1, text="Save", command=self.save_user_data) #Нужно дописать когда будет функция
        self.save_button.grid(row=3, column=1)

    def success_info(self):
        msg = "Data is synchronized"
        mb.showinfo("Success", msg)

    def show_error_ip(self):
        msg = "The IP address is filled in incorrectly!"
        mb.showerror("Error", msg)

    def show_error_copy(self):
        msg = "Fill in all the fields!"
        mb.showerror("Error", msg)


    def save_user_data(self):
        try:
            ipaddress.ip_address(self.ip_entry.get())
        except ValueError:
            self.show_error_ip()