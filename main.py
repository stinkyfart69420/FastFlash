import os

# This software is copyrighted.

print("This script requires sudo to function properly. Please enter your password to proceed.")
os.system(f"sudo e")

def select_linux_distro():
    print("Select an option:")
    print("1. Choose from predefined ISOs")
    print("2. Use a local ISO file")
    print("0. Exit")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        print("Select Linux distro to download:")
        print("1. Arch Linux")
        print("2. Fedora")
        print("3. Debian")
        print("4. Alpine Linux")
        print("5. openSUSE")
        print("6. Gentoo")
        print("7. NixOS")
        print("8. Manjaro")
        print("9. EndeavourOS")
        print("10. Linux Mint")
        print("11. Artix Linux (openrc base)")
        choice = input("Enter your choice (1-11): ")
        distros = {
            '1': 'https://au.mirrors.cicku.me/archlinux/iso/2024.03.01/archlinux-2024.03.01-x86_64.iso',
            '2': 'https://mirror.arizona.edu/fedora/linux/releases/39/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-39-1.5.iso',
            '3': 'https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-11.1.0-amd64-standard.iso',
            '4': 'http://dl-cdn.alpinelinux.org/alpine/v3.14/releases/x86_64/alpine-standard-3.14.2-x86_64.iso',
            '5': 'https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso',
            '6': 'https://distfiles.gentoo.org/releases/amd64/autobuilds/20240312T171909Z/install-amd64-minimal-20240312T171909Z.iso',
            '7': 'https://channels.nixos.org/nixos-23.11/latest-nixos-minimal-x86_64-linux.iso',
            '8': 'https://download.manjaro.org/xfce/23.1.3/manjaro-xfce-23.1.3-minimal-240113-linux66.iso',
            '9': 'https://mirrors.urbanwave.co.za/endeavouros/iso/EndeavourOS_Galileo-Neo-2024.01.25.iso',
            '10': 'https://mirrors.cicku.me/linuxmint/iso/stable/21.3/linuxmint-21.3-cinnamon-64bit.iso',
            '11': 'https://iso.artixlinux.org/weekly-iso/artix-base-openrc-20240304-x86_64.iso'
        }
        return distros.get(choice, None)
    elif choice == '2':
        custom_iso = input("Enter the path to your own ISO file: ")
        if os.path.exists(custom_iso):
            return custom_iso
        else:
            print("File not found.")
            return None
    else:
        print("Invalid choice.")
        return None

def download_iso(distro_url):
    os.system(f"wget {distro_url}")

def select_drive():
    print("Select the drive to flash the Linux distro:")
    drives = os.listdir('/dev/')
    for i, drive in enumerate(drives):
        print(f"{i+1}. {drive}")
    choice = int(input("Enter the drive number: "))
    selected_drive = drives[choice - 1]
    return selected_drive

def flash_distro(iso_path, drive):
    print(f"Flashing {iso_path} to {drive}...")
    os.system(f"sudo dd if={iso_path} of=/dev/{drive} bs=4M status=progress")

def main():
    iso_path = select_linux_distro()
    if iso_path is None:
        print("Invalid choice. Exiting.")
        return

    if iso_path.startswith("http"):
        download_iso(iso_path)
        iso_path = os.path.basename(iso_path)
    
    drive = select_drive()
    
    confirmation = input(f"WARNING: All partitions on /dev/{drive} will be erased. Continue? (yes/no): ")
    if confirmation.lower() == 'yes':
        os.system(f"sudo cfdisk /dev/{drive}")
        os.system(f"sudo umount /dev/{drive}*")
        flash_distro(iso_path, drive)
        print("Flashing complete.")
    else:
        print("Operation aborted.")

if __name__ == "__main__":
    main()
