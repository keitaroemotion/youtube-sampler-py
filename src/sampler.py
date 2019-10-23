#!/usr/bin/env python3

from pytube import YouTube
import os
import re
import subprocess
import sys

options = [x for x in sys.argv if x.startswith("-") ]
nums    = [x for x in sys.argv if re.search("^\d+$", x)]
wavs    = [x for x in sys.argv if x.endswith(".wav")]

def help():
    print("")
    print("sampler --wav ... convert file to youtube")
    print("")

def syscall(command):
    subprocess.call(command, shell=True)

def mp4_to_wav(video_name):
    wav_ext = video_name.replace(".mp4", "")
    syscall("ffmpeg -i %s -ab 160k -ac 2 -ar 44100 -vn %s.wav" % (video_name, wav_ext))

def sample(wavfile, start, duration=5):
    wavroot = wavfile.replace(".wav", "")
    syscall("ffmpeg -ss %d -t %d -i %s %s-%d%d.wav" % (start, duration, wavroot, start, duration))

def download():
    urls = [x for x in sys.argv if x.startswith("https://www.youtube.com/watch")]
    for url in urls:
        print("now downloading %s...." % url)
        YouTube(url)     \
            .streams     \
            .first()     \
            .download()

def update_filenames():
    for r, d, f in os.walk("."):
        for file in f:
            if '.mp4' in file:
                os.rename(file, file.replace(" ", ""))

def pwd():
    os.chdir(os.path.dirname(__file__))
    return os.getcwd()

if ("-h" in options) or ("help" in sys.argv):
    help()
elif("--wav" in options):
    download        ()
    update_filenames()
    for r, d, f in os.walk("."):
        for file in f:
            if '.mp4' in file:
                mp4_to_wav(os.path.join(r, file))

elif("--sample"):
    if len(nums) == 0:
        print("\nYou need to input start time(0~...)\n")
 
    start = nums[0]
    duration = nums[1] if nums[1] else 5
    if len(wavs) == 0:
        print("\nYou need to input wav file\n")
    sample(wavs[0], start, duration)
else:
    help()
