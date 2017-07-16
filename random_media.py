'''

random_media_LINUX_EDITION_PY.py
Jeremiah Bushau

Gathers and plays a specified number of files from a specified media library in VLC.

'''

import datetime
import os
import random
import subprocess
import time
import vlc

class Manager():
    def __init__(self):
        self.catagories = {
            'tv': ('/media/arab/Seagate Backup Plus Drive/Completed Media/TV/'),
            'movies': ('/media/arab/Seagate Backup Plus Drive/Completed Media/Movies/'),
            'anime': ('/media/arab/Seagate Backup Plus Drive/Completed Media/Anime/')
        }
        self.instance = vlc.Instance()
        self.player = self.instance.media_list_player_new()

    def create_all_media_list(self, catagory, all_media_array):
        for path, subdirs, files in os.walk(catagory):
            for file in files:
                if file.lower().endswith(('.mkv', '.m4v', '.mp4', '.divx', '.avi')):
                    all_media_array.append(os.path.join(path, file))


    def random_selection_from_media(self, in_array, out_array):
        random_selection = str(random.choice(in_array))
        if random_selection not in (out_array):
            out_array.append(random_selection)


    def get_selections(self, num, in_array, out_array):
        for i in range(int(num)):
            self.random_selection_from_media(in_array, out_array)

    def play(self, cat, num):
        if self.player.is_playing() != 0:
            return
        all_media = []
        self.create_all_media_list(self.catagories[cat], all_media)
        playlist = []
        self.get_selections(num, all_media, playlist)
        playlist = self.instance.media_list_new(playlist)
        self.player.set_media_list(playlist)
        # clean this up
        p = self.instance.media_player_new()
        p.toggle_fullscreen()
        self.player.set_media_player(p)
        self.player.play()

    def next(self):
        self.player.next()

    def prev(self):
        self.player.previous()

    def stop(self):
        self.player.stop()
