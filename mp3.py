import tkinter as tk
# from mutagen.mp3 import MP3
import vlc 
import time
   
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
	def play_func(self):
		soundFile.play()
		# time.sleep(audio_len)


root = tk.Tk()
root.title("Song Streamer")
root.geometry("300x150")
app = Application(master=root)
app.mainloop()
			

