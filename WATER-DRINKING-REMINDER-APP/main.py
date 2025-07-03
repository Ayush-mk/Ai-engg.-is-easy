import time
from winotify import Notification

while True:
    toast = Notification(
        app_id="Water Reminder 💧",
        title="Time to Drink Water!",
        msg="Stay hydrated, take a sip! 💦",
        duration="short"  # "short" = ~5 seconds
    )
    toast.show()
    time.sleep(60*60)  


