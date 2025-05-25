import schedule
import time
import threading

def check_market():
    print("[定時任務] 檢查市場狀態...")

def start_scheduler():
    schedule.every(1).minutes.do(check_market)

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    threading.Thread(target=run_scheduler, daemon=True).start()
