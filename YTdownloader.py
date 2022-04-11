from pytube import YouTube
from moviepy.editor import VideoFileClip
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def mp3Convert(filename):
    video = VideoFileClip(filename)
    video.audio.write_audiofile(filename[:-4] + ".mp3")
    video.close()


SAVE_PATH = "file path goes here."

getLink = input(Fore.GREEN + "Enter YouTube link: ")
usr_extention = input(Fore.MAGENTA + "Do you want to convert to mp3 format: ")
dwnld_file = YouTube(getLink)

print(Fore.BLACK + Back.YELLOW + f" Video Title: {dwnld_file.title} ")

for stream in dwnld_file.streams:
    print(Fore.CYAN + str(stream))
    
#gets the lowest resolution (this can be changed)
dwnld_file = dwnld_file.streams.get_lowest_resolution()
test = dwnld_file.download(SAVE_PATH)

#converts downloaded file to mp3 format (does not overwrite)
if usr_extention.lower() == "y":
    mp3Convert(test)
    print(Fore.BLACK + Back.GREEN + " Converted to mp3 ")

else:
    print(Fore.BLACK + Back.GREEN + " Completed ")
