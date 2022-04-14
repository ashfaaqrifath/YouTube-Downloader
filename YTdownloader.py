from pytube import YouTube
from pytube import Playlist
from moviepy.editor import VideoFileClip
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


root = tk.Tk()
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Downloader v3.0.0")
root.config(background="PaleGreen1")


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



def elements():

    app_banner = Label(root, text="YouTube Downloader",
                        padx=15,
                        pady=15,
                        font="SegoeUI 14",
                        bg="palegreen1",
                        fg="red")
    app_banner.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)

    yt_link = Label(root,
                        text="Enter link :",
                        bg="salmon",
                        pady=5,
                        padx=5)
    yt_link.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                            width=35,
                            textvariable=link_entry,
                            font="Arial 14")
    #tkinter copy paste
    root.linkText.bind_class("Entry", "<Button-3><ButtonRelease-3>", click_menu)
    root.linkText.grid(row=2,
                        column=1,
                        pady=5,
                        padx=5,
                        columnspan=2)

    folder_label = Label(root,
                            text="Folder :",
                            bg="salmon",
                            pady=5,
                            padx=9)
    folder_label.grid(row=3,
                        column=0,
                        pady=5,
                        padx=5)

    root.file_browse_text = Entry(root,
                                    width=27,
                                    textvariable=download_path,
                                    font="Arial 14")
    root.file_browse_text.grid(row=3,
                                column=1,
                                pady=5,
                                padx=5)

    file_browse = Button(root,
                        text="Browse",
                        command=browse_file,
                        width=10,
                        bg="bisque",
                        relief=GROOVE)
    file_browse.grid(row=3,
                    column=2,
                    pady=1,
                    padx=1)

    mp4_button = Button(root,
                        text="Download mp4",
                        command=download_mp4,
                        width=10,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE)
    mp4_button.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)

    mp3_button = Button(root,
                        text="Download mp3",
                        command=download_mp3,
                        width=10,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE)
    mp3_button.grid(row=4,
                    column=2,
                    pady=20,
                    padx=20)


def browse_file():
    download_Directory = filedialog.askdirectory()
    download_path.set(download_Directory)


def download_mp4():

    youtube_link = link_entry.get()
    download_folder = download_path.get()
    get_item = YouTube(youtube_link)
    file_stream = get_item.streams.get_lowest_resolution()
    file_stream.download(download_folder)
    messagebox.showinfo("Download Success", f"Downloaded video : {get_item.title}")


def download_mp3():

    youtube_link = link_entry.get()
    download_folder = download_path.get()
    get_item = YouTube(youtube_link)
    file_stream = get_item.streams.get_lowest_resolution()
    file_Convert = file_stream.download(download_folder)

    video = VideoFileClip(file_Convert)
    video.audio.write_audiofile(file_Convert[:-4] + ".mp3")
    video.close()
    os.remove(file_Convert)
    messagebox.showinfo("Download Success", f"Downloaded audio : {get_item.title}")


link_entry = StringVar()
download_path = StringVar()

elements()
makeMenu(root)

root.mainloop()
