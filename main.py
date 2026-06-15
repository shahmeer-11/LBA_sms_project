
import tkinter as tk
from gui_app import LbaGuiApp

def main():
    root = tk.Tk()
    app = LbaGuiApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()