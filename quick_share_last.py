import platform
import pywinauto
import pyautogui
from pywinauto.keyboard import send_keys
from pynput import keyboard


all_participants = [["triad"], [1, 2, 3, 4], [5, 6], [7, 8, 9]]
placeholder_rooms = 5

def on_escape():
    print("quit")

def on_activate_i():
    print('<ctrl>+<shift>+i pressed')
    h.stop()
def on_activate_go():
    send_keys('%s')
    try:
        app = pywinauto.Application(backend="uia").connect(title="Wählen Sie ein Fenster oder eine Anwendung, die Sie freigeben möchten")
        pos = pyautogui.position()
        sharing_window = app.window(title="Wählen Sie ein Fenster oder eine Anwendung, die Sie freigeben möchten").ListItem5.set_focus().click_input()
        pyautogui.moveTo(pos)
        send_keys('{ENTER}%{TAB}')
    except:
        print("no action")

with keyboard.GlobalHotKeys({
        '<shift>+<alt>+r': on_activate_go,
        '<alt>+d': on_activate_go,
        '<ctrl>+<alt>+i': on_activate_i}) as h:
    h.join()

