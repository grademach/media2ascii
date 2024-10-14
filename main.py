import av
import os
import time
import pydub
import threading
from pydub.playback import play
from get_frame import image_to_ascii

AUDIO = True
VIDEO_DIR = "./bad_apple.mp4"
FRAMES_DIR = os.getcwd() + "./frames/"
TERMINAL_RES = (50, 40)

if not os.path.exists(FRAMES_DIR):
    os.makedirs(FRAMES_DIR)

for file in os.listdir(FRAMES_DIR):
    os.remove(FRAMES_DIR + file)

vid = av.open(VIDEO_DIR)
frame_rate = vid.streams.video[0].average_rate

def play_audio():
    audio = pydub.AudioSegment.from_file(VIDEO_DIR, "mp4")
    play(audio)


total_frames = vid.streams.video[0].frames
for f in vid.decode(video=0):
    percentage = round((f.index/total_frames) * 100)
    os.system(f"title Loading frames - {percentage}%")
    f.to_image().save(f"./frames/{f.index}.jpg", quality=80)

if AUDIO:
    audio_thread = threading.Thread(target=play_audio)
    audio_thread.start()
for frame in range(vid.streams.video[0].frames):
    os.system(f"title Frame - {frame}")
    print("/r"+image_to_ascii(FRAMES_DIR + str(frame) + ".jpg", TERMINAL_RES))
    time.sleep(1/float(frame_rate+8.4))