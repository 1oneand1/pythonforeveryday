import time

seconds = 0
minutes = 0
hours = 0
while True:
    time.sleep(1)
    seconds += 1
    if seconds == 60:
        seconds = 0 # Reset seconds
        minutes += 1
        if minutes == 60:
            minutes = 0 # Reset minutes
            hours += 1
            print(f"{hours:02d}:{minutes:02d}:{seconds:02d} this is the time.")
        print(f"{hours:02d}:{minutes:02d}:00 has passed since the start of the watch")
    else:
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
