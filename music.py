from pygame import mixer



def menu_music():
   mixer.init()
   mixer.music.load("xDeviruchi - Title Theme .wav")
   mixer.music.play(-1)