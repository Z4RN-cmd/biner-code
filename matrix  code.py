import random
import time


GREEN = "\033[92m"
RESET = "\033[0m"

while True:
    matrix = ""
    for i in range(150):
        matrix += random.choice(["0", "1"])
    
    print(GREEN + matrix + RESET)
    time.sleep(0.05)  