#!/usr/bin/env python

from pytube import YouTube
import os
import subprocess
import sys

options = [x for x in sys.argv if x.startswith("-")]

def help():
    print("")
    print("sampler --wav ... convert file to youtube")
    print("")

def mp4_to_wav(video_name):
    wav_ext = video_name.replace(".mp4", "")
    command = "ffmpeg -i %s -ab 160k -ac 2 -ar 44100 -vn %s.wav" % (video_name, wav_ext)
    subprocess.call(command, shell=True)

def download():
    urls = [x for x in sys.argv if x.startswith("https://www.youtube.com/watch")]
    for url in urls:
        print("now downloading %s...." % url)
        YouTube(url)     \
            .streams     \
            .first()     \
            .download()

def pwd():
    os.chdir(os.path.dirname(__file__))
    return os.getcwd()

if ("-h" in options) or ("help" in sys.argv):
    help()
elif("--wav" in options):
    download  ()
    for r, d, f in os.walk("."):
        for file in f:
            if '.mp4' in file:
                mp4_to_wav(os.path.join(r, file))
else:
    help()
