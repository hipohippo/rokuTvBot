from roku import Roku
from telegram import Update
from telegram.ext import ContextTypes


async def roku_action(roku: Roku, query_data: str, update: Update, context: ContextTypes.DEFAULT_TYPE):
    if query_data == "poweron":
        roku.poweron()
    elif query_data == "poweroff":
        roku.poweroff()
    elif query_data == "home":
        roku.home()
    elif query_data == "select":
        roku.select()
    elif query_data == "volumeup":
        [roku.volume_up() for i in range(5)]
    elif query_data == "volumedown":
        [roku.volume_down() for i in range(5)]
    elif query_data == "netflix":
        roku["Netflix"].launch()
    elif query_data == "hbo":
        roku["HBO Max"].launch()
    else:
        raise ValueError(f"unsupported action {query_data}")
