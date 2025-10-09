import tkinter as tk
from truckdwell.gui.app import Application

if __name__ == "__main_":
  root = tk.Tk()
  root.geometry('700x285+600+200')
  root.resizable(False, False)
  app = Application(root)
  root.mainloop()
