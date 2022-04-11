import time
import keyboard
import pyautogui
import threading
import logging
import psutil
import sys
import os
import time
import win32api
import win32con
import ctypes
import PIL
import cv2

from win32gui import GetWindowText, GetForegroundWindow
class Mode:
    def __init__(self, name, buttons):
        self.buttons = buttons or []

    def start(self):
        for btn in self.buttons:
            btn.start()
        return

class Button:
    def __init__(self, name, file_name, x1, y1, x2, y2):
        self.name = name
        self.file_name = file_name
        self.x1 = x1 or 0
        self.y1 = y1 or 0
        self.x2 = x2 or 1920
        self.y2 = y2 or 1080
    
    def start(self):
        x1, y1, x2, y2 = Utilities.GetWindowRectFromName("CROSSFIRE")
        btn = pyautogui.locateCenterOnScreen(Utilities.resource_path(self.file_name), region=(x1, y1, x2, y2), grayscale=True, confidence=0.70)
        if btn is not None:
            pyautogui.moveTo(btn)
            Utilities.click()
            logging.info(f"Clicked {self.name}")
            time.sleep(0.1)

class Bot:
    def __init__(self):
        self.init_modes()

    anti_idle_delay = 10
    enable_anti_idle = False
    tdm = None
    za = None
    rza = None
    arcadia = None
    # is_paused = False
    def set_delay(self, delay):
        self.anti_idle_delay = delay
        logging.info(f"Delay set to {self.anti_idle_delay} seconds")
    def toggle_anti_idle(self):
        if self.enable_anti_idle is True:
            self.set_anti_idle(False)
        else:
            self.set_anti_idle(True)
    def set_anti_idle(self, enabled):
        logging.info("Press F4 to enable anti idle, F5 to disable")
        if enabled:
            logging.info("Anti Idle: Enabled")
            self.enable_anti_idle = True
        else:
            logging.info("Anti Idle: Disabled")
            self.enable_anti_idle = False
    def init_modes(self):
        buttons = []
        # buttons.append(Button("Ready", "assets/ready-2.png", 690, 410, 777, 457))
        # buttons.append(Button("Join Game", "assets/join-game.png", 690, 410, 777, 457))
        # buttons.append(Button("Ok", "assets/za-ok.png", 675, 525, 780, 570))
        buttons.append(Button("Ready", "assets/ready-2.png", 0, 0, 1920, 1080))
        buttons.append(Button("Join Game", "assets/join-game.png", 0, 0, 1920, 1080))
        buttons.append(Button("Ok", "assets/za-ok.png", 0, 0, 1920, 1080))
        self.tdm = Mode("TDM", buttons)

        buttons = []
        buttons.append(Button("Ready", "assets/ready-2.png", 0, 0, 1920, 1080))
        buttons.append(Button("Start", "assets/start-2.png", 0, 0, 1920, 1080))
        buttons.append(Button("Join", "assets/join-game.png", 0, 0, 1920, 1080))
        buttons.append(Button("Confirm", "assets/za-confirm.png", 0, 0, 1920, 1080))
        buttons.append(Button("Ok", "assets/za-ok.png", 0, 0, 1920, 1080))
        self.za = Mode("ZA", buttons)

        buttons = []
        buttons.append(Button("Confirm", "assets/confirm.png", 0, 0, 1920, 1080))
        buttons.append(Button("Ready", "assets/ready.png", 0, 0, 1920, 1080))
        buttons.append(Button("Accept", "assets/accept.png", 0, 0, 1920, 1080))
        buttons.append(Button("Ok", "assets/za-ok.png", 0, 0, 1920, 1080))
        buttons.append(Button("Confirm", "assets/za-confirm.png", 0, 0, 1920, 1080))
        self.rza = Mode("RZA", buttons)

        buttons = []
        buttons.append(Button("Confirm", "assets/3/arcadia/confirm.png", 0, 0, 1920, 1080))
        buttons.append(Button("Ready", "assets/3/arcadia/join.png", 0, 0, 1920, 1080))
        buttons.append(Button("Accept", "assets/3/arcadia/ok.png", 0, 0, 1920, 1080))
        buttons.append(Button("Ok", "assets/3/arcadia/ok2.png", 0, 0, 1920, 1080))
        buttons.append(Button("Confirm", "assets/3/arcadia/ready.png", 0, 0, 1920, 1080))
        self.arcadia = Mode("Arcadia", buttons)

    def controller(self, mode):
        self.enable_anti_idle
        start = time.time()
        end = time.time()
        self.is_exit = False
        logging.info("Auto Ready: Started")
        logging.info("Press F4 to enable anti idle, F5 to disable")
        while True:
            try:
                if self.is_exit:
                    break
                while not keyboard.is_pressed('f2'):
                    if keyboard.is_pressed('f3'):
                        self.is_exit = True
                    if self.is_exit:
                        break
                    if keyboard.is_pressed('f5'):
                        self.set_anti_idle(False)
                        time.sleep(1)
                    if keyboard.is_pressed('f4'):
                        self.set_anti_idle(True)
                        time.sleep(1)
                    end = time.time()
                    elapsed = end-start
                    if (elapsed > self.anti_idle_delay and Utilities.is_cf_active()):
                        if mode == 1:
                            self.rza.start()
                        elif mode == 2:
                            self.za.start()
                        elif mode == 3:
                            self.tdm.start()
                        elif mode == 4:
                            self.arcadia.start()

                        if self.enable_anti_idle:
                            self.anti_idle()
                        start = time.time()
                    continue

                logging.info("Auto Ready: Paused")
                while not keyboard.is_pressed('f1'):
                    if keyboard.is_pressed('f3'):
                        self.is_exit = True
                        break
            except Exception as e:
                logging.info(e)
                continue
        logging.info("Terminated")
        quit()

    def anti_idle(self):
        Utilities.click()
        pyautogui.press('enter') 
        for i in range(3):
            Utilities.click()
        pyautogui.press('enter') 
        pyautogui.press('enter') 

    def get_mode(self):
        logging.info("Press 1 for ZA Public Match")
        logging.info("Press 2 for ZA")
        logging.info("Press 3 for TDM")
        logging.info("Press 4 for ZA Normal")
        # logging.info("Press 3 for normal room")
        while True:
            if keyboard.is_pressed('1'):
                return 1
            if keyboard.is_pressed('4'):
                return 2
            if keyboard.is_pressed('4'):
                return 3
            if keyboard.is_pressed('4'):
                return 4

    def worker(self):
        mode = self.get_mode()
        time.sleep(1)
        logging.info("Press F1 to Start")
        logging.info("Press F2 to Pause")
        logging.info("Press F3 to exit")
        try:
            if mode > 4:
                quit()
            self.controller(mode)
        except KeyboardInterrupt:
            quit()
    
    def start(self):
        self.t1 = threading.Thread(target=self.worker, args=[])
        self.t1.daemon = True
        self.t1.start()
    def stop(self):
        self.is_exit = True

class Utilities:
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
    def click():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.1)
 

    def is_cf_active():
        if GetWindowText(GetForegroundWindow()) == "CROSSFIRE":
            return True
        return False

    def GetWindowRectFromName(name:str)-> tuple:
        hwnd = ctypes.windll.user32.FindWindowW(0, name)
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(hwnd, ctypes.pointer(rect))
        return (rect.left, rect.top, rect.right, rect.bottom)