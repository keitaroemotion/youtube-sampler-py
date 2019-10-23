#!/usr/bin/env python

from pytube import YouTube
import sys

options = [x for x in sys.argv if x.startswith("-")]

def help():
    print("")
    print("sampler --download ... download .wav file from youtube")
    print("")

if ("-h" in options) or ("help" in sys.argv):
    help()
elif("--download" in options):
    urls = [x for x in sys.argv if x.startswith("https://www.youtube.com/watch")]
    for url in urls:
        print("now downloading %s...." % url)
        YouTube(url)     \
            .streams     \
            .first()     \
            .download()
