import time


def countdowntimer():
    time1 = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    while time1 > -1:
        minute, second = (time1 // 60, time1 % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        # Update the time
        window.update()
        time.sleep(1)
        if time1 == 0:
            seconds.set('00')
            minutes.set('00')
            hours.set('00')
        time1 -= 1
