from telegram_bot.bot import start_bot
from scheduler.market_timer import start_scheduler

def main():
    print("[INFO] 啟動 AI 投資監控助手 V4.1")
    start_scheduler()
    start_bot()

if __name__ == "__main__":
    main()
