from pytube import YouTube
from pytube import Playlist
from moviepy.editor import VideoFileClip
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


def elements():

    app_banner = Label(root, text="YouTube Downloader", padx=15, pady=15, font="Rubik 14", fg="red")
    app_banner.grid(row=1, column=1, pady=10, padx=5, columnspan=3)
    
    # copyright_label = Label(root, text="Copyright © Ashfaaq Rifath 2022", padx=50, pady=50, font="Rubik 14", fg="black")
    # copyright_label.grid(row=1, column=2, pady=10, padx=5, columnspan=3)

    root.ytLink = Entry(root, width=35, textvariable=getLink, font="Rubik 14")
    root.ytLink.insert(0, "Enter YouTube link")
    root.ytLink.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    root.dwnld_path = Entry(root, width=27, textvariable=download_path, font="Rubik")
    root.dwnld_path.insert(0, "Download Folder")
    root.dwnld_path.grid(row=3, column=1, pady=5, padx=5)

    fileBrowse = Button(root, text="Browse", command=browseFile, width=10,)
    fileBrowse.grid(row=3, column=2, pady=1, padx=1)

    download_button = Button(root, text="Download", command=downloadVideo, width=20, pady=10, padx=15, font="Rubik")
    download_button.grid(row=4, column=1, pady=20, padx=20)


def browseFile():

    save_path = filedialog.askdirectory()
    download_path.set(save_path)


def downloadVideo():

    youtube_link = getLink.get()
    download_folder = download_path.get()
    dwnld_file = YouTube(youtube_link)
    quality = dwnld_file.streams.get_lowest_resolution()
    quality.download(download_folder)

    messagebox.showinfo("Download Success")


root = tk.Tk()

root.geometry("520x280")
root.resizable(0, 0)
root.title("YouTube Downloader")

getLink = StringVar()
download_path = StringVar()

elements()

root.mainloop()
