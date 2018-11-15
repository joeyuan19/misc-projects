import sys
import time
if len(sys.argv) < 2:
    print("Provide file argument")
    sys.exit()

with open(sys.argv[1],'r') as f:
    song = tuple(line.strip() for line in f)

speed = 10

for line in song:
    print(line)
    time.sleep(speed)

