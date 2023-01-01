from pytube import YouTube
from colorama import Fore,Back
from pyfiglet import figlet_format
from urllib.request import urlopen
from time import sleep
import sys
from pyperclip import paste
from os import system
from pytube.cli import on_progress
from tkinter.filedialog import askdirectory
from threading import Thread


def slprint(text,seconds=.1):#a function to print text slowy
    from time import sleep
    import sys
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(seconds)


print(Fore.LIGHTRED_EX+figlet_format("YT Downloader",font="slant"),Fore.RESET)#print the name of programe

while True:#check internet
    try: 
        slprint(Fore.LIGHTYELLOW_EX+"Checking internet...\n"+Fore.RESET, .06)
        urlopen("https://youtube.com")#to check if internet works
        slprint(Fore.LIGHTGREEN_EX+"✔ Youtube server is reachable!\n\n"+Fore.RESET, .06)
        print("Press Enter to get the copied link")
        url = input(Fore.CYAN+"URL: "+Fore.RESET)
        if url == "":
            url = paste()
        break
    except:
        slprint(Fore.LIGHTRED_EX+"✘ No Internet\n"+Fore.RESET)#print no internet
        slprint(Fore.LIGHTYELLOW_EX+"Press Enter to try again!"+Fore.RESET,.05    )
        input("\n")

while True:#Get and check url
    try:
        yt=YouTube(url,on_progress_callback=on_progress)#check vedio
        break
    except:
        slprint(Fore.RED+"Wrong URl\n"+Fore.RESET, .1)#Say that url is wrong
        print("Press Enter to get the copied link")
        url = input(Fore.CYAN+"URL: "+Fore.RESET)#url input try again
        if url == "":
            url = paste()

print(u"Video title: "+Fore.MAGENTA+yt.title+Fore.RESET)#print video title


###################################################################################



slprint(Fore.LIGHTYELLOW_EX+"Getting video qualites...\n"+Fore.RESET)#print geting aualities



normal_quality_list = ["144p","360p","720p"]#has the qualities       "normal"
availaple_normal_quality_list = []#has the available streems         "normal"
availaple_normal_quality_list_names = []#has the available qualities "normal"

non_normal_quality_list = []
availaple_normal_quality_list = []
availaple_normal_quality_list_names =[]
#https://youtu.be/E-81lwxXIwQ
for res in normal_quality_list: #getting normal video quality 
    try:
        r = yt.streams.filter(res=res,progressive=True)[-1]
        availaple_normal_quality_list.append(r)
        availaple_normal_quality_list_names.append(res)
    except:
        continue


try:            #get audio streem
    r = yt.streams.filter(only_audio=True)[-1]
    availaple_normal_quality_list.append(r)
    availaple_normal_quality_list_names.append("audio")
except:
    pass

##########
num = 1 ##################################################show qualities##########
slprint(Fore.LIGHTCYAN_EX+"Video qualites\n"+Fore.RESET)#print Video qualites  ####
for res in availaple_normal_quality_list_names:                                #####
    slprint(Fore.LIGHTYELLOW_EX+"[{}] ".format(num)+res+Fore.RESET+"\n",.01)   ######
    num += 1                                                                   #####
###################################################################################

while True:#get choice from user
    slprint(Fore.LIGHTCYAN_EX+"Choose: "+Fore.RESET)
    choice = input(Fore.LIGHTMAGENTA_EX)
    try:
        int(choice)
        if int(choice) <= len(availaple_normal_quality_list_names) and int(choice)>0:
            break
        elif int(choice) > len(availaple_normal_quality_list_names) or int(choice)==0 or int(choice)<0:
            slprint(Fore.LIGHTRED_EX+"Out of range!\n"+Fore.RESET,.02)
    except:
        slprint(Fore.LIGHTRED_EX+"Enter a Number!\n"+Fore.RESET)
#chose download folder
slprint(Fore.LIGHTCYAN_EX+"choose Folder to download\n"+Fore.RESET)
sleep(1)
path = askdirectory()

choice=int(choice)-1



slprint(Fore.LIGHTYELLOW_EX+"Downloading..\n"+Fore.RESET)

availaple_normal_quality_list[choice].download(path)
print("\n")

slprint(Fore.LIGHTGREEN_EX+"Video successfuly downloaded!\n"+Fore.RESET)

system("cls")

slprint(Fore.GREEN+"Done!\n"+Fore.RESET)
slprint("This programe was developed py...\n")

def loop():
    list = [Fore.MAGENTA,Fore.BLUE,Fore.CYAN,Fore.GREEN,Fore.YELLOW,Fore.RED]
    while True:
        for i in list:
            print(figlet_format("Developed py ...",font="slant"))
            print(i+figlet_format("Amr Mohamed",font="slant")+Fore.RESET)
            sleep(.3)
            system("cls")
loop()