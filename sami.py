import os
import time
import random


try:
    os.system('git add *')
    time.sleep(5)
    os.system(f'git commit -m {"update + " + str(random.randint(1, 1000))}')
    time.sleep(5)
    os.system('git push origin main --force')
    time.sleep(5)
    print("-------------------------------------------------------------------------")
    print("---------------metidaaaa 🥵🥵🥵... digo... Done!!!-----------------------")
    print("-------------------------------------------------------------------------")
except Exception as error:
    print("--------------------------------------------------------------------------")
    print(f"-----------------------------------{error}------------------------------")
    print("-------------------------------------------------------------------------")
