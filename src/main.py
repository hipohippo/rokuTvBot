import logging
import sys
from configparser import SectionProxy
from typing import Union

from telegram.ext import CommandHandler, CallbackQueryHandler, Application

from hipo_telegram_bot_common.bot_config.bot_config_parser import parse_from_ini
from hipo_telegram_bot_common.bot_factory import BotBuilder
from hipo_telegram_bot_common.common_handler import heart_beat_job
from hipo_telegram_bot_common.keyboard.handler import init_static_keyboard, start_static_keyboard_handler
from roku_tv_bot.handler import text_input_handler, execute_query
from roku_tv_bot.roku_tv_bot_config import RokuTvBotConfig

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

"""
REF: https://developer.roku.com/docs/developer-program/dev-tools/external-control-api.md
ECP/SSDP 

keypress is essentially done through POST request

// type
requests.post("http://[host]:[port]/keypress/LIT_d")

// volume up 
requests.post("http://[host]:[port]/keypress/VolumeUp")
"""


def build_bot_app(bot_config_dict: Union[dict, SectionProxy]) -> Application:
    bot_config = RokuTvBotConfig(bot_config_dict)
    app = (
        BotBuilder(bot_config_dict["bot_token"], bot_config)
        .add_handlers(
            [
                CommandHandler("start", start_static_keyboard_handler),
                CommandHandler("text", text_input_handler),
                CallbackQueryHandler(execute_query),
            ]
        )
        .add_repeating_jobs([(heart_beat_job, {"first": 5, "interval": 4 * 60 * 60})])
        .build()
    )
    return app


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    app = build_bot_app(parse_from_ini(sys.argv[1]))
    app.run_polling()
