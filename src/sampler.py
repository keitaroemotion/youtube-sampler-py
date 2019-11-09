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
    print("sampler --play [mp3|wav]                      ... play music file")
    print("sampler --wav [url1] [url2]                   ... convert file to youtube")
    print("sampler --sample [start] [duration] [wavfile] ... sample wav file")
    print("")

def syscall(command):
    print("\n[%s]\n" % command)
    subprocess.call(command, shell=True)

def mp4_to_wav(video_name):
    wav_ext = video_name.replace(".mp4", "")
    syscall("ffmpeg -i %s -ab 160k -ac 2 -ar 44100 -vn %s.wav" % (video_name, wav_ext))

def sample(wavfile, start, duration):
    wavroot = wavfile.replace(".wav", "")
    syscall("ffmpeg -ss %s -t %s -i %s %s-%s-%s.wav" % (start, duration, wavfile, wavroot, start, duration))

def download():
    urls = [x for x in sys.argv if x.startswith("https://www.youtube.com/watch")]
    if len(urls) == 0:
        print("\nYou need to specify the video url!\n")
        sys.exit()

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

elif("--play" in options):
    songs = [x for x in sys.argv if re.search(".*\.(wav|mp3)$", x)]
    if (len(songs) == 0):
        songs = [x for x in os.listdir(".") if re.search(".*\.(wav|mp3)$", x)]

    for song in songs: 
        syscall("afplay {}".format(song))

elif("--wav" in options):
    download        ()
    update_filenames()
    for r, d, f in os.walk("."):
        for file in f:
            if '.mp4' in file:
                mp4_to_wav(os.path.join(r, file))

elif("--sample" in options):
    if len(nums) == 0:
        print("\nYou need to input start time(0~...)\n")
        sys.exit()
 
    start = nums[0]
    duration = nums[1] if len(nums) > 1 else 5
    print("duration: %s" % duration)

    if len(wavs) == 0:
        print("\nYou need to input wav file\n")
        sys.exit()

    sample(wavs[0], start, duration)

else:
    help()
