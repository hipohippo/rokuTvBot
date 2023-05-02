from hipo_telegram_bot_common.keyboard.button import Button


def get_static_keyboard_layout():
    keyboard_layout = [
        [
            Button("Power On", "poweron"),
            Button("Power Off", "poweroff"),
        ],
        [
            Button("Home", "home"),
            Button("Select", "select"),
        ],
        [
            Button("Volume +5", "volumeup"),
            Button("Volume -5", "volumedown"),
        ],
        [
            Button("Netflix", "netflix"),
            Button("HBO", "hbo"),
        ],
    ]
    return keyboard_layout
