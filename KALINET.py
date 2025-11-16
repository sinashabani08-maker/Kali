#coded B279《■》KINGHacker《■》

#modluse of script
import subprocess
import sys
import os

#color's'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
h = '\033[3;67m'
belu = '\033[1;34m'
su = '\033[0m'

#banner
subprocess.run(["python", "banner2.py"])

#menu
subprocess.run(["python", "menu.py"])

#script
BU = int(input('>-----Your---Dastor----》'))
if BU == 2:
		      subprocess.run(["python","KALI.py"])	
elif BU == 4:
		      subprocess.run(["python","help.py"])
elif BU == 6:
	          subprocess.run(["python","Abot.py"])
else:
	print(f"""\n{h}{yellow}
     ⚠️ ┌─────────────────┐ ⚠️
        │    N O T           │
        │   PERMITTED        │
        └─────────────────┘
        ███████████████████
   """)

print(f'\n{su}')