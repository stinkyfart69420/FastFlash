import os

os.system("sudo apt install git")
print("Downloading latest version...")
os.system("git clone https://github.com/stinkyfart69420/FastFlash")
print("Downloaded succesfully. Launching FastFlash...")
os.system("cd FastFlash && cd update && python3 main.py")
print("Cleaning up before exiting...")
os.system("rm -rf FastFlash")
