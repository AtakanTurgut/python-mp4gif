from moviepy.editor import *

video = VideoFileClip("videoGame.mp4")
video.write_gif("gifGame.gif")