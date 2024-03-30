import os
import sys

if len(sys.argv) > 1:
            if sys.argv[1]== "--noupdate":
                os.system("cd update && python3 main.py")
exit()

print("Downloading latest version...")
os.system("git clone https://github.com/stinkyfart69420/FastFlash")
print("Downloaded succesfully. Launching FastFlash...")
os.system("cd FastFlash && cd update && python3 main.py")
os.system("rm -rf FastFlash")
