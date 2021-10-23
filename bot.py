import time
import keyboard
import pyautogui
import win32api
import win32con
import threading
import logging
import sys
import os
try:
    import tkinter as tk # Python 3.x
    import tkinter.scrolledtext as ScrolledText
except ImportError:
    import Tkinter as tk # Python 2.x
    import ScrolledText

anti_idle_delay = 1
enable_anti_idle = False
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

class myGUI(tk.Frame):

    # This class defines the graphical user interface 

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.build_gui()

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
        st = ScrolledText.ScrolledText(self, state='disabled')
        st.configure(font='TkFixedFont')
        st.grid(column=0, row=1, sticky='w', columnspan=4)

        # Create textLogger
        text_handler = TextHandler(st)

        # Logging configuration
        logging.basicConfig(filename=None,
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s - %(message)s')        

        # Add the handler to logger
        logger = logging.getLogger()        
        logger.addHandler(text_handler)

def resource_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)

def ready_za():
    ready2 = pyautogui.locateCenterOnScreen(resource_path('assets/ready-2.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    start2 = pyautogui.locateCenterOnScreen(resource_path('assets/start-2.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    join = pyautogui.locateCenterOnScreen(resource_path('assets/join-game.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    za_confirm = pyautogui.locateCenterOnScreen(resource_path('assets/za-confirm.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    za_ok = pyautogui.locateCenterOnScreen(resource_path('assets/za-ok.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    if za_confirm is not None:
        pyautogui.moveTo(za_confirm)
        click()
        logging.info("Clicked Confirm")
        time.sleep(0.1)

    elif za_ok is not None:
        pyautogui.moveTo(za_ok)
        click()
        logging.info("Clicked Ok Result")
        time.sleep(0.1)

    elif ready2 is not None:
        pyautogui.moveTo(ready2)
        click()
        logging.info("Clicked Ready")
        time.sleep(0.1)

    elif join is not None:
        pyautogui.moveTo(join)
        click()
        logging.info("Clicked Join Game")
        time.sleep(0.1)
    elif start2 is not None:
        state = "lobby"
        pyautogui.moveTo(start2)
        click()
        logging.info("Clicked Start")
        time.sleep(0.1)

def ready_rza():
    confirm = pyautogui.locateCenterOnScreen(resource_path('assets/confirm.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    ready = pyautogui.locateCenterOnScreen(resource_path('assets/ready.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.90)
    accept = pyautogui.locateCenterOnScreen(resource_path('assets/accept.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    if confirm is not None:
        pyautogui.moveTo(confirm)
        click()
        time.sleep(0.1)
        logging.info("Clicked Confirm")
    elif ready is not None:
        pyautogui.moveTo(ready)
        click()
        logging.info("Clicked Ready")
        time.sleep(0.1)
    elif accept is not None:
        pyautogui.moveTo(accept)
        click()
        logging.info("Clicked Accept")
        time.sleep(0.1)

def ready_tdm():
    ready2 = pyautogui.locateCenterOnScreen(resource_path('assets/ready-2.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    start2 = pyautogui.locateCenterOnScreen(resource_path('assets/start-2.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    join = pyautogui.locateCenterOnScreen(resource_path('assets/join-game.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    za_confirm = pyautogui.locateCenterOnScreen(resource_path('assets/za-confirm.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    za_ok = pyautogui.locateCenterOnScreen(resource_path('assets/za-ok.png'), region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    if za_confirm is not None:
        pyautogui.moveTo(za_confirm)
        click()
        logging.info("Clicked Confirm")
        time.sleep(0.1)

    elif za_ok is not None:
        pyautogui.moveTo(za_ok)
        click()
        logging.info("Clicked Ok Result")
        time.sleep(0.1)

    elif ready2 is not None:
        pyautogui.moveTo(ready2)
        click()
        logging.info("Clicked Ready")
        time.sleep(0.1)

    elif join is not None:
        pyautogui.moveTo(join)
        click()
        logging.info("Clicked Join Game")
        time.sleep(0.1)
    elif start2 is not None:
        state = "lobby"
        pyautogui.moveTo(start2)
        click()
        logging.info("Clicked Start")
        time.sleep(0.1)

def controller(mode):
    global enable_anti_idle
    start = time.time()
    end = time.time()
    is_exit = False
    while True:
        if is_exit:
            break
        logging.info("Auto Ready: Started")
        logging.info("Press F4 to enable anti idle, F5 to disable")
        while not keyboard.is_pressed('f2'):
            if keyboard.is_pressed('f3'):
                is_exit = True
                break
            if keyboard.is_pressed('f5'):
                logging.info("Anti Idle: Disable")
                enable_anti_idle = False
                time.sleep(1)
            if keyboard.is_pressed('f4'):
                logging.info("Anti Idle: Enable")
                enable_anti_idle = True
                time.sleep(1)
            end = time.time()
            elapsed = end-start
            if (elapsed > anti_idle_delay):
                if mode == '1':
                    ready_rza()
                elif mode == '2':
                    ready_za()
                elif mode == '3':
                    ready_tdm()

                if enable_anti_idle:
                    anti_idle()
                start = time.time()
            continue

        logging.info("Auto Ready: Paused")
        while not keyboard.is_pressed('f1'):
            if keyboard.is_pressed('f3'):
                is_exit = True
                break
    logging.info("Terminated")
    quit()

def anti_idle():
    click()
    pyautogui.press('enter') 
    for i in range(3):
        click()
    pyautogui.press('enter') 
    pyautogui.press('enter') 

def get_mode():
    logging.info("Press 1 for Ranked ZA")
    logging.info("Press 2 for ZA")
    # logging.info("Press 3 for normal room")
    while True:
        if keyboard.is_pressed('1'):
            return 1
        if keyboard.is_pressed('2'):
            return 2
        if keyboard.is_pressed('3'):
            return 3

def worker():
    mode = get_mode()
    time.sleep(1)
    logging.info("Press F1 to Start")
    logging.info("Press F2 to Pause")
    logging.info("Press F3 to exit")
    try:
        if mode > 2:
            quit()
        controller(mode)
    except KeyboardInterrupt:
        quit()
    

def quit():
    global root
    root.quit()

def main():
    myGUI(root)

    t1 = threading.Thread(target=worker, args=[])
    t1.start()
    root.mainloop()

    t1.join()
root = tk.Tk()

main()