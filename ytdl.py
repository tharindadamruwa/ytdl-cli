class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def download():
    try:
        from pytube import YouTube
    except:
        print()
        print(bcolors.OKGREEN + "Installing package...!")
        print()
        import sys,os
        os.system("pip install pytube")
    import os,sys
    print(bcolors.WARNING + "[1] Android    [2] Windows   [3] Linux")
    print()
    path = str(input(bcolors.OKGREEN + "Enter Your Platform >> >> >> " + bcolors.ENDC))
    print()
    if path == "1":
        os.system("termux-setup-storage")
        dlpath = "/sdcard/Download"
    elif path == "2":
        usn = os.getlogin()
        dlpath = "C:/Users/" + usn + "/Downloads"
    elif path == "3":
        dlpath = "/home/Downloads"
    else:
        print("Your input is not valid.. Restart programme" + bcolors.ENDC)
        print()

    link = str(input(bcolors.OKBLUE + "Enter your YouTube video link >> >> >> " + bcolors.OKGREEN))
    print()
    print(bcolors.WARNING + "Getting Data...!")
    print()
    try:        
        yt = YouTube(link)
    except:
        print(f'Video {link} is unavailable, skipping.')
        print()
        link = str(input(bcolors.OKBLUE + "Enter your YouTube video link >> >> >> " + bcolors.OKGREEN))
        print()
        print(bcolors.WARNING + "Getting Data...!")
        print()
        yt = YouTube(link)

    vname = yt.title
    vdescrip = yt.description
    print("Success")
    print()
    print(bcolors.FAIL + "------------Video Title------------")
    print(bcolors.OKCYAN + vname)
    print()
    print(bcolors.FAIL + "------------Video Description------------")
    print(bcolors.OKCYAN + vdescrip)
    print()
    print(bcolors.FAIL + "[1] Hd Download      [2] Low Download      [3] Audio Download")
    print()
    chq = str(input(bcolors.OKBLUE + "Enter your choice >> >> >> " + bcolors.OKGREEN))
    print()
    if chq == '1':
        print("Downloading...!")
        print()
        yt.streams.get_highest_resolution().download(dlpath)
        print("Succeed..! Check " + dlpath)
        print(bcolors.ENDC)
    elif chq == '2':
        print("Downloading...!")
        print(bcolors.ENDC)
        yt.streams.get_lowest_resolution().download(dlpath)
        print("Succeed..! Check " + dlpath)
        print(bcolors.ENDC)
    elif chq == "3":
        print("Downloading...!")
        print(bcolors.ENDC)
        out = yt.streams.filter(only_audio=True).first().download(dlpath)
        base, ext = os.path.splitext(out)
        new = base + '.mp3'
        os.rename(out, new)
        print("Succeed..! Check " + dlpath)
        print(bcolors.ENDC)
    else:
        print("Your input is not valid.. Restart programme" + bcolors.ENDC)
        print()

def menu():
    import sys,os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bcolors.WARNING + "    ")
    print("██╗   ██╗████████╗██████╗ ██╗     ")
    print("╚██╗ ██╔╝╚══██╔══╝██╔══██╗██║     ")
    print(" ╚████╔╝    ██║   ██║  ██║██║     ")
    print("  ╚██╔╝     ██║   ██║  ██║██║     ")
    print("   ██║      ██    ██████╔╝███████╗")
    print("   ╚═╝      ╚═╝   ╚═════╝ ╚══════╝")
    print()
    print(" [1] Start               [2] Go To Our GitHub")
    print()
    ch = str(input(bcolors.OKCYAN + "Enter Your Choice >> >> >> " + bcolors.OKGREEN))
    print()
    if ch == "1":
        download()
    elif ch == "2":
        import webbrowser
        webbrowser.open("https://github.com/tharindadamruwa")
        print(bcolors.ENDC)
    else:
        print("Your input is not valid.. Restart programme" + bcolors.ENDC)

menu()