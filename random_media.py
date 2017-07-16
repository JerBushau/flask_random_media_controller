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


# class media_list(list):
#     'media list class'
#     def __init__(self):
#         self = []

#     def play_list(self):
#         self.insert(0, 'vlc')
#         self.insert(1, '-f')
#         subprocess.Popen(self, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


#     def log_list(self):
#         log_file = open(db, 'a')
#         time_is = time.time()
#         formated_time = datetime.datetime.fromtimestamp(time_is).strftime('%Y-%m-%d %H:%M:%S')
#         log_file.write('\n' + formated_time)
#         log_file.write('-------------------------'.join('\n{}: {}\n'
#               ''.format(*i) for i in enumerate(self, 1)))


class Manager():
    def __init__(self):
        self.catagories = {
            'tv': ('/media/jer/Seagate Backup Plus Drive/Completed Media/TV/'),
            'movies': ('/media/jer/Seagate Backup Plus Drive/Completed Media/Movies/'),
            'anime': ('/media/jer/Seagate Backup Plus Drive/Completed Media/Anime/')
        }
        self.player = vlc.MediaListPlayer()


    def create_media_list(self, catagory, all_media_array):
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


    def run(self, cat, num):
        if self.player.is_playing() != 0:
            return
        all_media = []
        playlist = []
        self.create_media_list(self.catagories[cat], all_media)
        self.get_selections(num, all_media, playlist)
        playlist = vlc.MediaList(playlist)
        self.player.set_media_list(playlist)
        self.player.play()

    def next(self):
        print(self.player.is_playing())
        self.player.next()

    def prev(self):
        self.player.previous()

    def stop(self):
        self.player.stop()
