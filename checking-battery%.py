# pip install psutil #
import psutil

# Battery sensor capture #
battery = psutil.sensors_battery()

# Battery percentage capture #
percent = str(battery.percent)

# Show result #
print(f'You currently have {percent}% battery')
