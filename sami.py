import os
import time


try:
    os.system('git add *')
    time.sleep(5)
    os.system('git commit -m "update"')
    time.sleep(5)
    os.system('git push origin main --force')
    time.sleep(5)
    print("Done")
except Exception as e:
    print(e)