from hipo_telegram_bot_common.keyboard.keyed_bot_config import KeyedBotConfig
from hipo_telegram_bot_common.util import format_white_list
from roku_tv_bot.keyboard import get_static_keyboard_layout


class RokuTvBotConfig(KeyedBotConfig):
    def __init__(self, config_dict: dict):
        super().__init__(
            config_dict["heart_beat_chat"],
            config_dict["error_notify_chat"],
            format_white_list(config_dict["white_list"]),
            "Roku TV Bot",
            get_static_keyboard_layout(),
        )
        self._roku_ip_address = config_dict["ip_address"]

    @property
    def ip_address(self):
        return self._roku_ip_address
