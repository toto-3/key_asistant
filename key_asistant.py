from configobj import ConfigObj
from pynput import keyboard
import PySimpleGUI as simplegui
import string
import re

QWERTY_LIST = list('qwertyuiopasdfghjkl;zxcvbnm,./')
KEY_LISTS = {k: k for k in QWERTY_LIST + list(string.punctuation + string.digits)} | \
            {f'{k}'.split('.')[1]: k for k in keyboard.Key}

[print(x) for x in KEY_LISTS]

ACT_LISTS = {
    '____' : [''       , 'shift'                  ],  # ToDo
    '1___' : ['1'       , '1'                      ],
    '2___' : ['2'       , '2'                      ],
    '3___' : ['3'       , '3'                      ],
    '4___' : ['4'       , '4'                      ],
    '5___' : ['5'       , '5'                      ],
    '6___' : ['6'       , '6'                      ],
    '7___' : ['7'       , '7'                      ],
    '8___' : ['8'       , '8'                      ],
    '9___' : ['9'       , '9'                      ],
    '0___' : ['0'       , '0'                      ],
    'A___' : ['A'       , 'a'                      ],
    'B___' : ['B'       , 'b'                      ],
    'C___' : ['C'       , 'c'                      ],
    'D___' : ['D'       , 'd'                      ],
    'E___' : ['E'       , 'e'                      ],
    'F___' : ['F'       , 'f'                      ],
    'G___' : ['G'       , 'g'                      ],
    'H___' : ['H'       , 'h'                      ],
    'I___' : ['I'       , 'i'                      ],
    'J___' : ['J'       , 'j'                      ],
    'K___' : ['K'       , 'k'                      ],
    'L___' : ['L'       , 'l'                      ],
    'M___' : ['M'       , 'm'                      ],
    'N___' : ['N'       , 'n'                      ],
    'O___' : ['O'       , 'o'                      ],
    'P___' : ['P'       , 'p'                      ],
    'Q___' : ['Q'       , 'q'                      ],
    'R___' : ['R'       , 'r'                      ],
    'S___' : ['S'       , 's'                      ],
    'T___' : ['T'       , 't'                      ],
    'U___' : ['U'       , 'u'                      ],
    'V___' : ['V'       , 'v'                      ],
    'W___' : ['W'       , 'w'                      ],
    'X___' : ['X'       , 'x'                      ],
    'Y___' : ['Y'       , 'y'                      ],
    'Z___' : ['Z'       , 'z'                      ],
    'TILD' : ['~'       , '~'                      ],
    'EXLM' : ['!'       , '!'                      ],
    'AT__' : ['@'       , '@'                      ],
    'HASH' : ['#'       , '#'                      ],
    'DLR_' : ['$'       , '$'                      ],
    'PERC' : ['%'       , '%'                      ],
    'CIRC' : ['^'       , '^'                      ],
    'AMPR' : ['&'       , '&'                      ],
    'ASTR' : ['*'       , '*'                      ],
    'UNDS' : ['_'       , '_'                      ],
    'PLUS' : ['+'       , '+'                      ],
    'PIPE' : ['|'       , '|'                      ],
    'COLN' : [':'       , ':'                      ],
    'DQUO' : ['"'       , '"'                      ],
    'QUES' : ['?'       , '?'                      ],
    'MINS' : ['-'       , '-'                      ],
    'EQL_' : ['='       , '='                      ],
    'BSLS' : ['\\'      , '\\'                     ],
    'SCLN' : [';'       , ';'                      ],
    "QUOT" : ["'"       , "'"                      ],
    'GRV_' : ['`'       , '`'                      ],
    'COMM' : [','       , ','                      ],
    'DOT_' : ['.'       , '.'                      ],
    'SLSH' : ['/'       , '/'                      ],
    'LPRN' : ['('       , '('                      ],
    'RPRN' : [')'       , ')'                      ],
    'LCBR' : ['{'       , '{'                      ],
    'RCBR' : ['}'       , '}'                      ],
    'LABK' : ['<'       , '<'                      ],
    'RABK' : ['>'       , '>'                      ],
    'LBRC' : ['['       , '['                      ],
    'RBRC' : [']'       , ']'                      ],
    'LEFT' : ['←'       , 'left'                   ],
    'DOWN' : ['↓'       , 'down'                   ],
    'RGHT' : ['→'       , 'right'                  ],
    'UP__' : ['↑'       , 'up'                     ],
    'HOME' : ['Home'    , 'home'                   ],
    'END_' : ['End'     , 'end'                    ],
    'PGUP' : ['PgUp'    , 'page_down'              ],
    'PGDN' : ['PgDn'    , 'page_up'                ],
    'TAB_' : ['Tab'     , 'tab'                    ],
    'ENT_' : ['Enter'   , 'enter'                  ],
    'ESC_' : ['Esc'     , 'esc'                    ],
    'BSPC' : ['BS'      , 'backspace'              ],
    'DEL_' : ['Delete'  , 'delete'                 ],
    'SPC_' : ['Space'   , 'space'                  ],
    'CTRL' : ['Ctrl'    , 'ctrl'                   ],
    'SHFT' : ['Shift'   , 'shift'                  ],
    'ALT_' : ['Alt'     , 'alt'                    ],
    'CMD_' : ['Cmd'     , 'cmd'                    ],
    'F1__' : ['F1'      , 'f1'                     ],
    'F2__' : ['F2'      , 'f2'                     ],
    'F3__' : ['F3'      , 'f3'                     ],
    'F4__' : ['F4'      , 'f4'                     ],
    'F5__' : ['F5'      , 'f5'                     ],
    'F6__' : ['F6'      , 'f6'                     ],
    'F7__' : ['F7'      , 'f7'                     ],
    'F8__' : ['F8'      , 'f8'                     ],
    'F9__' : ['F9'      , 'f9'                     ],
    'F10_' : ['F10'     , 'f10'                    ],
    'F11_' : ['F11'     , 'f11'                    ],
    'F12_' : ['F12'     , 'f12'                    ],
    'ENG_' : ['ENG'     , ''                       ],
    'JPN_' : ['JPN'     , ''                       ],
    'SYM_' : ['SYM'     , ''                       ],
    'NUM_' : ['NUM'     , ''                       ],
    # 'SAVE' : ['Save'    , 'ctrl'       , 's'       ],
    # 'CLSE' : ['Close'   , 'ctrl'       , 'w'       ],
    # 'PAST' : ['Paste'   , 'ctrl'       , 'v'       ],
    # 'COPY' : ['Copy'    , 'ctrl'       , 'c'       ],
    # 'CUT_' : ['Cut'     , 'ctrl'       , 'x'       ],
    # 'ALL_' : ['All'     , 'ctrl'       , 'a'       ],
    # 'EXPL' : ['Explr'   , 'cmd'        , 'e'       ],
    # 'DT__' : ['DskTp'   , 'cmd'        , 'd'       ],
    # 'LOCK' : ['Lock'    , 'cmd'        , 'l'       ],
    # 'FIND' : ['Find'    , 'ctrl'       , 'f'       ],
    # 'REPL' : ['Replc'   , 'ctrl'       , 'r'       ],
    # 'RENM' : ['ReNm'    , 'f2'                     ],
}

class KeyAsistant:
    def __init__(self) -> None:
        self._config = ConfigObj('config.ini')
        mode = self._config['default']
        self._key_remapper = KeyRemapper(mode, self._config[mode])

    @property
    def mode(self):
        return self._key_remapper.mode

    @property
    def key_remapper(self):
        return self._key_remapper

    def press(self, key):
        print(f'KeyAsistant.press() called')
        self._key_remapper.key_press(key)
        
    def release(self, key):
        print(f'KeyAsistant.release() called')
        self._key_remapper.key_release(key)

class KeyRemapper(dict):
    def __init__(self, mode, config) -> None:
        self._mode = mode
        self._config = config
        self._keys = {}
        self._btn_colors = self._config['btn_colors']
        for qwerty, tap, hold in zip(QWERTY_LIST,
                                     re.sub(r'[\n ]', '', self._config['tap']).split('|'),
                                     re.sub(r'[\n ]', '', self._config['hold']).split('|')):
            self._keys[qwerty] = CustomKey(tap, hold)
        print(self._keys)

    @property
    def mode(self):
        return self._mode

    def create_layout(self):
        return[
            [simplegui.T(f'Mode : {self._mode}' ,key='LBL_TITLE')],
            [
                self.create_buttons(QWERTY_LIST[ 0:10]),
                self.create_buttons(QWERTY_LIST[10:20]),
                self.create_buttons(QWERTY_LIST[20:30]),
            ]
        ]

    def create_buttons(self, keys):
        buttons = []
        for key in keys:
            buttons.append(
                simplegui.Button(
                    self._keys[key].disp_name,
                    key=f'BTN_{key}',
                    disabled=True,
                    button_color=self._btn_colors,
                    font=('HackGenNerd', 24),
                    size=(5, 2),
                    pad=((0, 0), (0, 0))
                )
            )
        return buttons
    
    def key_press(self, key):
        print(f'KeyRemapper.key_press() called')
        print(f'key = {key}')
        window.find_element(f'BTN_{key}').Update(button_color=self._btn_colors[::-1])
        sending_keys.append(key)
        print(f'sending_keys = {sending_keys}')
        self._keys[key].tap()

    def key_release(self, key):
        print(f'KeyRemapper.key_release() called')
        print(f'key = {key}')
        window.find_element(f'BTN_{key}').Update(button_color=self._btn_colors)
        sending_keys.remove(key)
        print(f'sending_keys = {sending_keys}')

sending_keys = []

class CustomKey:
    def __init__(self, tap, hold) -> None:
        self._tap_name , *self._tap_acts  = ACT_LISTS[tap]
        self._hold_name, *self._hold_acts = ACT_LISTS[hold]
    
    @property
    def disp_name(self):
        return f'{self._hold_name}\n{self._tap_name}'

    @property
    def hold_action(self):
        return self._hold_action

    def tap(self):
        for act in self._tap_acts:
            keyboard.Controller().press(KEY_LISTS[act])
        for act in self._tap_acts[:-1]:
            keyboard.Controller().release(KEY_LISTS[act])


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
        key_asistant.press(key_string(key))
    
def key_release(key, injected):
    print(f'key_release() called')
    print(f'injected = {injected}')
    if injected == 0:
        key_asistant.release(key_string(key))
    if key == keyboard.Key.esc:
        return False

def win32_event_filter(msg, data):
    print('################')
    print(f'win32_event_filter called. {msg} {data.vkCode} {keyboard_listener._suppress}')
    keyboard_listener._suppress = not sending_keys
    print(f'keyboard_listener._suppress = {keyboard_listener._suppress}')
    return True

if __name__== '__main__':

    keyboard_listener = keyboard.Listener(
        on_press=key_press,
        on_release=key_release, 
        win32_event_filter=win32_event_filter,
        suppress=True
    )
    keyboard_listener.start()

    key_asistant = KeyAsistant()
    window = simplegui.Window(
        'Keyboard Asistant', 
        key_asistant.key_remapper.create_layout(),
        # no_titlebar=True,
        alpha_channel=.8,
        keep_on_top=True,
        grab_anywhere=True,
        margins=(0,0),
    )
    while True:
        event, values = window.read()
        print(event, values)
        if event in (simplegui.WIN_CLOSED, 'Exit'):
            break
