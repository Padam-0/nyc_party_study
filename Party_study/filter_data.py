import datetime
import subprocess

first_sat = datetime.date(2014, 4, 5)
last_sat = datetime.date(2015, 6, 27)
week = datetime.timedelta(days=7)
day = datetime.timedelta(days=1)

i = 0
current_sat = first_sat

while current_sat != last_sat:
    current_sat = first_sat + week * i
    current_sun = current_sat + day

    subprocess.call(["./greper.sh", str(current_sat),
    str(current_sun), 'yellow_trips_2015Q2.csv', 'yellow_sats.csv'])

    i += 1
