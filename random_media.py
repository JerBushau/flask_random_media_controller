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

db = ('/home/arab/Projects/flask_random_media_controller/database/logs.txt')

catagories = {
    'tv': ('/media/arab/Seagate Backup Plus Drive/Completed Media/TV/'),
    'movies': ('/media/arab/Seagate Backup Plus Drive/Completed Media/Movies/'),
    'anime': ('/media/arab/Seagate Backup Plus Drive/Completed Media/Anime/')
}

class media_list(list):
    'media list class'
    def __init__(self):
        self = []

    def play_list(self):
        self.insert(0, 'vlc')
        self.insert(1, '-f')
        subprocess.Popen(self, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def log_list(self):
        log_file = open(db, 'a')
        time_is = time.time()
        formated_time = datetime.datetime.fromtimestamp(time_is).strftime('%Y-%m-%d %H:%M:%S')
        log_file.write('\n' + formated_time)
        log_file.write('-------------------------'.join('\n{}: {}\n'
              ''.format(*i) for i in enumerate(self, 1)))


def create_media_list(catagory, all_media_array):
    for path, subdirs, files in os.walk(catagory):
        for file in files:
            if file.lower().endswith(('.mkv', '.m4v', '.mp4', '.divx', '.avi')):
                all_media_array.append(os.path.join(path, file))


def random_selection_from_media(in_array, out_array):
    random_selection = str(random.choice(in_array))
    if random_selection not in (out_array):
        out_array.append(random_selection)


def get_selections(num, in_array, out_array):
    for i in range(int(num)):
        random_selection_from_media(in_array, out_array)


def run(cat, num):
    all_media = media_list()
    playlist = media_list()
    create_media_list(catagories[cat], all_media)
    get_selections(num, all_media, playlist)
    playlist.log_list()
    playlist.play_list()

