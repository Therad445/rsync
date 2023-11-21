# main.py

from tkinter import Tk
from tkinter_app import RsyncGUI

# if "DISPLAY" not in os.environ:
#             # install and start Xvfb
#             os.system("Xvfb :99 -screen 0 1024x768x16 &")
#             os.environ["DISPLAY"] = ":99"
# Xvfb :99 -screen 0 1024x768x16 &
# DISPLAY"] = ":99


def main():
    root = Tk()
    RsyncGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
