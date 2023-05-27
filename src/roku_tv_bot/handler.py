import logging

import pandas as pd
import requests
from roku import Roku
from telegram import Update, CallbackQuery, Message
from telegram.ext import ContextTypes

from hipo_telegram_bot_common.util import restricted
from roku_tv_bot.query import roku_action
from roku_tv_bot.roku_tv_bot_config import RokuTvBotConfig


@restricted
async def text_input_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not (update.message or update.message.text):
        logging.info(f"update invalid: {update.message}")
        return

    def extract_text(raw_text):
        return raw_text[6:]

    type_text = extract_text(update.message.text)
    context.bot_data["bot_config"].roku.literal(type_text)
    await update.message.reply_text(text="message sent to TV")


@restricted
async def execute_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query: CallbackQuery = update.callback_query  # button callback data
    tv_connected = check_tv_connection(context)
    if not tv_connected:
        status_msg = "TV not connected"
    elif query.data is None:
        status_msg = "invalid query"
    else:
        await roku_action(context.bot_data["roku"], query.data, update, context)
        status_msg = f"selected {query.data.upper()} at {pd.Timestamp.now().strftime('%T.%f')}"
    await query.answer(text=status_msg)


def check_tv_connection(context: ContextTypes.DEFAULT_TYPE) -> bool:
    """
    check tv connection.
    * new instance if not defined
    * connect if defined but not connected
    * raise if fail to connect
    :param context:
    :return:
    """
    bot_config: RokuTvBotConfig = context.bot_data["bot_config"]
    if not "roku" in context.bot_data:
        context.bot_data["roku"] = Roku(bot_config.ip_address)
    roku: Roku = context.bot_data["roku"]

    try:
        roku.power_state
        return True
    except requests.exceptions.ConnectTimeout:
        logging.error("cannot connect to roku tv device")
        return False
