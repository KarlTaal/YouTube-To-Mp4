import pytube
import sys
import os
#pip install pytube3
# peale seda teha muudatusi allalaetud skriptis link:
# https://stackoverflow.com/questions/62098925/why-my-youtube-video-downloader-only-downloads-some-videos-and-for-other-videos

if not os.path.exists('songs'):
    os.makedirs('songs')
    
links  = []
with open("laulud.txt", "r", encoding="UTF-8") as f:
    for r in f:
        links.append(r.strip())

print("Starting...")
for i in range(len(links)):
    pytube.YouTube(links[i]).streams.filter(only_audio=True).first().download("songs/")
    progress = round((i+1) / len(links) * 100)
    sys.stdout.write("Download progress: %d%%   \r" % (progress) )
    sys.stdout.flush()
    if i == len(links)-1:
        print()

print("Done")