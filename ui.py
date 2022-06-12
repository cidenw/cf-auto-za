import tkinter as tk # Python 3.x
import tkinter.scrolledtext as ScrolledText
import time
import logging
from bot import Bot
from datetime import datetime
import datetime
import ctypes
from tkinter import simpledialog
class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

class Menu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.bot = None
        self.build_gui()
        self.check_expiry()

    def check_expiry(self):
        CurrentDate = datetime.datetime.now()
        print(CurrentDate)

        ExpectedDate = "1/5/2023 1:00"
        ExpectedDate = datetime.datetime.strptime(ExpectedDate, "%d/%m/%Y %H:%M")
        logging.info(f"Valid until {ExpectedDate}")

        if CurrentDate > ExpectedDate:
            ctypes.windll.user32.MessageBoxW(0, "Expired na, chat mo Yorushika Komorebi", "Expired", 1)
            self.root.destroy()
    def build_gui(self):                    
        # Build GUI
        self.root.title('Ranked ZA Auto - Yoru')
        self.root.option_add('*tearOff', 'FALSE')
        self.grid(column=0, row=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(2, weight=1, uniform='a')
        self.grid_columnconfigure(3, weight=1, uniform='a')

        # Add text widget to display logging info
        self.st = ScrolledText.ScrolledText(self, state='disabled')
        self.st.configure(font='TkFixedFont')
        self.st.grid(column=0, row=1, sticky='w', columnspan=4)
        # Create textLogger
        text_handler = TextHandler(self.st)

        # Logging configuration
        logging.basicConfig(filename=None,
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s - %(message)s')        

        # Add the handler to logger
        logger = logging.getLogger()        
        logger.addHandler(text_handler)

        self.button = tk.Button(self, text="Exit",
                           command=self.CloseWindow, font=("Arial", 12))
        self.button.grid()

        self.start_button = tk.Button(self, text="Start",
                           command=self.start_bot, font=("Arial", 12))
        self.start_button.grid()

        self.stop_button = tk.Button(self, text="Stop",
                           command=self.stop_bot, font=("Arial", 12))
        self.stop_button.grid()

        self.delay_button = tk.Button(self, text="Delay",
                           command=self.delay, font=("Arial", 12))
        self.delay_button.grid()

        self.idle_button = tk.Button(self, text="Anti Idle",
                           command=self.anti_idle, font=("Arial", 12))
        self.idle_button.grid()
    def anti_idle(self):
        if self.bot is None:
            return
        self.bot.toggle_anti_idle()
    def delay(self):
        delay_str = simpledialog.askstring(title="Change Delay",
                                  prompt="Anti Idle Delay:")
        delay = None
        try:
            delay = int(delay_str)
            if delay < 1:
                raise ValueError
        except:
            logging.info("Not a valid delay")
            return
        if self.bot is None:
            return
        self.bot.set_delay(delay)
    def CloseWindow(self):
        self.root.destroy()
    def start_bot(self):
        self.bot = Bot()
        self.bot.start()
    def stop_bot(self):
        if self.bot is None:
            return
        self.bot.stop()