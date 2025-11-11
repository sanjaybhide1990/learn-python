import psutil
import datetime

battery = psutil.sensors_battery()
is_Plugged = battery.power_plugged
current_battery_percentage = battery.percent
usable_duration = str(datetime.timedelta(seconds=battery.secsleft))

if is_Plugged:
    print(f"Charging!!. Currently it's at ({current_battery_percentage}%)")
else: 
    print(f"Currently battery is at {current_battery_percentage}%. At the current rate, it can be used for another {usable_duration} hours")
