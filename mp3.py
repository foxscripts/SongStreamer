import tkinter as tk
from bs4 import BeautifulSoup
import requests
# from mutagen.mp3 import MP3
import vlc 
import time
 

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

url = requests.get('http://musichunterz.in/pSo.php', headers=headers)
urlContent =BeautifulSoup(url.content, "lxml")
  
audio = "Pink Floyd - We Don't Need No Education.mp3"
# audioFile = MP3(audio)
# audio_len= audioFile.info.length
soundFile = vlc.MediaPlayer(audio)

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.myWindow()

	def myWindow(self):
		self.play_music = tk.Button(root, text="Play Music", command = self.play_func)
		self.play_music.pack(side="top")
		for x in range(1,5):
			self.song_list = tk.Button(root, text=" ", command = self.get_list, width=50)
			self.song_list.pack()
	def play_func(self):
		soundFile.play()
		# time.sleep(audio_len)
	def get_list(self):
		for song_name in urlContent.find_all('td'):
			song_name = song_name.text
			self.song_list["text"]+=song_name


root = tk.Tk()
root.title("Song Streamer")
root.geometry("1500x700")
app = Application(master=root)
app.mainloop()
			

