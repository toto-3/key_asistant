from configobj import ConfigObj
from pynput import keyboard
import PySimpleGUI as simplegui
import string
import re

QWERTY_LIST = list('qwertyuiopasdfghjkl;zxcvbnm,./')
KEY_LISTS = {k: k for k in QWERTY_LIST + list(string.punctuation + string.digits)} | \
            {f'{k}'.split('.')[1]: k for k in keyboard.Key}

ALIASES = {
    '←'       : 'left'      ,
    '↓'       : 'down'      ,
    '→'       : 'right'     ,
    '↑'       : 'up'        ,
    'PgUp'    : 'page_down' ,
    'PgDn'    : 'page_up'   ,
    'Ent'     : 'enter'     ,
    'BS'      : 'backspace' ,
    'Del'     : 'delete'    ,
    'Spc'     : 'space'     ,
    'Shft'    : 'shift'     ,
}

class KeyLayer:
    def __init__(self, config):
        self._button_color = config['button_color']
        self._keys = {}
        for qwerty, tap, hold in zip(QWERTY_LIST, self.parse_keys(config['taps']), self.parse_keys(config['holds'])):
            self._keys[qwerty] = CustomKey(tap, hold)

    def parse_keys(self, keys):
        return re.sub(r'[\n ]', '', keys).split('|')
    
    def press(self, key):
        print(f'KeyLayer.key_press() called')
        print(f'key = {key}')
        if (mode := self._keys[key].tap()) is not None:
            self.change_mode(mode)

    def release(self, key):
        print(f'KeyLayer.key_release() called')
        print(f'key = {key}')
    


class CustomKey:
    def __init__(self, tap, hold):
        self._tap = tap
        self._hold = hold
    
    @property
    def disp_name(self):
        return f'{self._hold}\n{self._tap}'

    def tap(self):
        # if self._tap in ['Eng', 'Jpn', 'Sym', 'Num']:
        #     return self._tap
        key = KEY_LISTS[ALIASES.get(self._tap, self._tap).lower()]
        keyboard.Controller().tap(key)



def update_window():
    window.find_element('MODE').Update(f'Mode : {mode}')
    for k in QWERTY_LIST:
        window.find_element(f'BTN_{k}').Update(f'Mode : {mode}')
        print(f'BTN_{k}')

def create_buttons(keys):
    buttons = []    # ToDo
    for key in keys:
        print(f'key=BTN_{key}')
        buttons.append(
            simplegui.Button(
                f'{key_layers[mode]._keys[key].disp_name}',
                key=f'BTN_{key}',
                disabled=True,
                button_color=config[mode]['button_color'],
                font=('HackGenNerd', 24),
                size=(5, 2),
                pad=((0, 0), (0, 0))
            )
        )
    return buttons

def key_string(key):
    print(f'key_string() called')
    print(f'key={key}')
    try:
        print(f'alphanumeric key {key.char}')
        return key.char
    except AttributeError:
        print(f'special key {key}')
        return key

def key_press(key, injected):
    print(f'key_press() called.')
    print(f'injected = {injected}')
    if injected == 0:
        key_name = key_string(key)
        print(f'key=BTN_{key_name}')
        # window.find_element(f'BTN_{key_name}').Update(button_color=config['button_color'][::-1])
        sending_keys.append(key_name)
        key_layers[mode].press(key_name)
    
def key_release(key, injected):
    print(f'key_release() called')
    print(f'injected = {injected}')
    if injected == 0:
        key_name = key_string(key)
        print(f'key=BTN_{key_name}')
        sending_keys.remove(key_name)
        key_layers[mode].release(key_name)
        # window.find_element(f'BTN_{key_name}').Update(button_color=config['button_color'])
    if key == keyboard.Key.esc:
        return False

def win32_event_filter(msg, data):
    print('################')
    print(f'win32_event_filter called. {msg} {data.vkCode}')
    print(f'sending_keys={sending_keys}')
    keyboard_listener._suppress = not sending_keys
    print(f'keyboard_listener._suppress={keyboard_listener._suppress}')
    return True

if __name__== '__main__':
    config = ConfigObj('config.ini')
    mode = config['default']
    key_layers = {mode: KeyLayer(config[mode]) for mode in ['Eng', 'Sym', 'Num']}
    sending_keys = []

    keyboard_listener = keyboard.Listener(
        on_press=key_press,
        on_release=key_release, 
        win32_event_filter=win32_event_filter,
        suppress=False
    )

    window = simplegui.Window(
        'Keyboard Asistant', 
        [
            [simplegui.T(f'Mode : {mode}' ,key='MODE')],
            [
                create_buttons(QWERTY_LIST[ 0:10]),
                create_buttons(QWERTY_LIST[10:20]),
                create_buttons(QWERTY_LIST[20:30]),
            ]
        ],
        # no_titlebar=True,
        alpha_channel=.8,
        keep_on_top=True,
        grab_anywhere=True,
        margins=(0,0),
    )

    # update_window()

    keyboard_listener.start()
    while True:
        event, values = window.read()
        print(event, values)
        if event in (simplegui.WIN_CLOSED, 'Exit'):
            break
