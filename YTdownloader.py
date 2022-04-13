from pytube import YouTube
from moviepy.editor import VideoFileClip
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def mp3Convert(filename):
    video = VideoFileClip(filename)
    video.audio.write_audiofile(filename[:-4] + ".mp3")
    video.close()

print('''
░█──░█ ▀▀█▀▀ 　 ░█▀▀▄ ░█▀▀▀█ ░█──░█ ░█▄─░█ ░█─── ░█▀▀▀█ ─█▀▀█ ░█▀▀▄ ░█▀▀▀ ░█▀▀█ 
░█▄▄▄█ ─░█── 　 ░█─░█ ░█──░█ ░█░█░█ ░█░█░█ ░█─── ░█──░█ ░█▄▄█ ░█─░█ ░█▀▀▀ ░█▄▄▀ 
──░█── ─░█── 　 ░█▄▄▀ ░█▄▄▄█ ░█▄▀▄█ ░█──▀█ ░█▄▄█ ░█▄▄▄█ ░█─░█ ░█▄▄▀ ░█▄▄▄ ░█─░█ v1.0.1
                          Copyright (c) Ashfaaq Rifath 2022''')


SAVE_PATH = "file path goes here."

getLink = input(Fore.GREEN + "Enter YouTube link: ")
usr_extention = input(Fore.MAGENTA + "Do you want to convert to mp3 format (y/n): ")
dwnld_file = YouTube(getLink)

print(Fore.BLACK + Back.YELLOW + f" Video Title: {dwnld_file.title} ")

for stream in dwnld_file.streams:
    print(Fore.CYAN + str(stream))

dwnld_file = dwnld_file.streams.get_lowest_resolution()
fileConvert = dwnld_file.download(SAVE_PATH)

if usr_extention.lower() == "y":
    mp3Convert(fileConvert)
    os.remove(fileConvert)
    print(Fore.BLACK + Back.GREEN + " Converted to mp3 ")

else:
    print(Fore.BLACK + Back.GREEN + " Request completed ")
