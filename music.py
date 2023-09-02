from pygame import mixer



def menu_music():
   mixer.init()
   mixer.music.load("xDeviruchi - Title Theme .wav")
   mixer.music.play(-1)


def head_music():
   mixer.init()
   mixer.music.load("xDeviruchi - Exploring The Unknown.wav")
   mixer.music.play(-1)

def story_music():
   mixer.init()
   mixer.music.load("xDeviruchi - Mysterious Dungeon.wav")
   mixer.music.play(-1)