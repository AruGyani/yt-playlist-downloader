import os
from pytube import Playlist

link = input("Enter playlist link: ")
playlist = Playlist(link)

os.mkdir(playlist.title)

print(playlist.title)

print("\nDownloading videos...")
for video in playlist.videos:
    video.streams.get_highest_resolution().download(playlist.title)
    print(video.title + " successfully downloaded")

print("\nFinished!\n")