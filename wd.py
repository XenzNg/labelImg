from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

my_observer = Observer()
sender_obj = None


class SignalSender(QWidget):
    updateHighlightSignal = pyqtSignal()


def set_sender_obj(obj):
    global sender_obj
    sender_obj = obj


def start(folder):
    my_event_handler = PatternMatchingEventHandler(["*"], ignore_patterns=None, ignore_directories=False,
                                                   case_sensitive=True)
    my_event_handler.on_any_event = lambda event: sender_obj.updateHighlightSignal.emit()
    my_observer.schedule(my_event_handler, folder, recursive=True)
    my_observer.start()
    return my_observer


def stop():
    my_observer.stop()
