import pytube
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import VideoFileClip
import webbrowser
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


root = tk.Tk()
root.geometry("600x370")
root.resizable(False, False)
root.title("YT Downloader v3.3.2")
root.config(background="#a30000")

p1 = PhotoImage(file = "ytd.png")
root.iconphoto(False, p1)


def makeMenu(w):
    global the_menu
    the_menu = tk.Menu(w, tearoff=0)
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")


def click_menu(e):
    w = e.widget
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))

    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))

    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


def callback(url):
    webbrowser.open_new_tab(url)


def elements():
    app_banner = Label(root, text="YouTube Downloader",
                        padx=15,
                        pady=15,
                        bg="#a30000",
                        fg="white",
                        font="Magneto 20 bold")
    app_banner.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)

    copyright_label = Label(root, text="Copyright © Ashfaaq Rifath - YT Downloader",
                        padx=0,
                        pady=0,
                        bg="#a30000",
                        fg="white",)
    copyright_label.grid(row=2,
                    column=1,
                    pady=0,
                    padx=0,
                    columnspan=3)

    yt_link = Label(root,
                        text="Enter link :",
                        bg="#00fbff",
                        pady=5,
                        padx=5,
                        font="Arial 10")
    yt_link.grid(row=3,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                            width=35,
                            textvariable=link_entry,
                            font="Arial 14")
    #tkinter copy paste
    root.linkText.bind_class("Entry", "<Button-3><ButtonRelease-3>", click_menu)
    root.linkText.grid(row=3,
                        column=1,
                        pady=5,
                        padx=5,
                        columnspan=2)

    folder_label = Label(root,
                            text="Save to :",
                            bg="#00fbff",
                            pady=5,
                            padx=9,
                            font="Arial 10")
    folder_label.grid(row=4,
                        column=0,
                        pady=5,
                        padx=5)

    root.file_browse_text = Entry(root,
                                    width=27,
                                    textvariable=download_path,
                                    font="Arial 14")
    root.file_browse_text.grid(row=4,
                                column=1,
                                pady=5,
                                padx=5)

    file_browse = Button(root,
                        text="Browse",
                        command=browse_file,
                        width=10,
                        bg="salmon",
                        relief=GROOVE)
    file_browse.grid(row=4,
                    column=2,
                    pady=1,
                    padx=1)

    m

def browse_file():
    download_Directory = filedialog.askdirectory()
    download_path.set(download_Directory)


def download_mp4():
    try:
        youtube_link = link_entry.get()
        itag = resolution()

        if "=" in youtube_link:
            download_folder = download_path.get()
            playlist = Playlist(youtube_link)
            for video in playlist.videos:
                print(video.title)
                playlist_res = video.streams.get_by_itag(itag)
                playlist_res.download(download_folder)
                messagebox.showinfo("Download Success", "Downloaded playlist")

        download_folder = download_path.get()
        get_item = YouTube(youtube_link)
        file_res = get_item.streams.get_by_itag(itag)
        file_res.download(download_folder)
        messagebox.showinfo("Download Success", f"Downloaded video : {get_item.title}")
    except:
        messagebox.showerror("Invalid Link", "Enter valid link")


def download_mp3():
    try:
        youtube_link = link_entry.get()
        download_folder = download_path.get()
        get_item = YouTube(youtube_link)
        file_res = get_item.streams.get_lowest_resolution()
        file_Convert = file_res.download(download_folder)

        video = VideoFileClip(file_Convert)
        video.audio.write_audiofile(file_Convert[:-4] + ".mp3")
        video.close()
        os.remove(file_Convert)
        messagebox.showinfo("Download Success", f"Downloaded audio : {get_item.title}")
    except:
        messagebox.showerror("Invalid Link", "Enter valid link")


var = IntVar()
link_entry = StringVar()
download_path = StringVar()

elements()
makeMenu(root)

root.mainloop()







# <<< Copyright (c) 2022 Ashfaaq Rifath - YT Downloader v3.3.2 >>>
