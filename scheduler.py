from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


def task():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(task, 'cron', day_of_week="fri", minute=15)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
