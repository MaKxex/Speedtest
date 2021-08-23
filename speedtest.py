import os
import subprocess

path , obj = os.path.split(__file__)
speedlst = subprocess.check_output([path + "/speedtest.exe"],shell=True).decode(encoding="utf-8").strip().split("\r\n")[2:-1]
for stat in speedlst:
    statlst = stat.strip().split(":")
    statName, statValue = statlst[0].strip(), statlst[1].strip()
    print(statName + " : " + statValue)

