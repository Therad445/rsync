# tkinter_app.py

from tkinter import *
from tkinter import filedialog
from rsync import Rsync


class RsyncGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rsync GUI")
        self.code = StringVar()

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

        self.local_radio = Radiobutton(master, text="Local copy", value="-azvh", variable=self.code)
        self.local_radio.grid(row=3, column=1)

        self.remote_radio = Radiobutton(master, text="Remote copy", value="-avz", variable=self.code)
        self.remote_radio.grid(row=3, column=2)

    def browse_source(self):
        source_dir = filedialog.askdirectory()
        self.source_entry.delete(0, END)
        self.source_entry.insert(0, source_dir)

    def browse_dest(self):
        dest_dir = filedialog.askdirectory()
        self.dest_entry.delete(0, END)
        self.dest_entry.insert(0, dest_dir)

    def copy(self):
        code = self.code.get()
        source_dir = self.source_entry.get()
        dest_dir = self.dest_entry.get()

        rsync = Rsync(code, source_dir, dest_dir)
        rsync.run()