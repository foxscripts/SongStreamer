import vlc 
import time
from mutagen.mp3 import MP3

audio = "Pink Floyd - We Don't Need No Education.mp3"
audioFile = MP3(audio)
audio_len= audioFile.info.length

soundFile = vlc.MediaPlayer(audio)
soundFile.play()

time.sleep(audio_len)