from pynput import keyboard
from pynput.mouse import Controller
import win32gui

w = win32gui
mouse = Controller()
pixels = 2


def on_press(key):
    try:
        assert key.char
        window_title = w.GetWindowText(w.GetForegroundWindow())
        if window_title[-1] != ']' or window_title[:8] != 'labelImg':
            assert False
    except Exception:
        return
    if key.char == 'w':
        mouse.move(0, -1 * pixels)
    if key.char == 'a':
        mouse.move(-1 * pixels, 0)
    if key.char == 's':
        mouse.move(0, 1 * pixels)
    if key.char == 'd':
        mouse.move(1 * pixels, 0)


def main():
    with keyboard.Listener(on_press=on_press) as listener:
        print('running keyboard-mouse shortcut')
        listener.join()


if __name__ == '__main__':
    main()
