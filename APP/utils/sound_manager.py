from gtts import gTTS
from playsound import playsound
import time
import os
char_added_path=os.path.join('APP','Files','Sounds','write_sound.wav')
char_deleted_path=os.path.join('APP','Files','Sounds','delete_sound.wav')
space_added_path=os.path.join('APP','Files','Sounds','space_sound.wav')
word_file_path=os.path.join('APP','Files','Sounds','voice_sound.wav')

class SoundPlayer():
    def play_char_added_sound(self):
        playsound(char_added_path,block=True)
    def play_char_deleted_sound(self):
        playsound(char_deleted_path,block=True)
    def play_space_added_sound(self):
        playsound(space_added_path,block=True)
    
    def play_text_sound(self,text:str):
        tts = gTTS(text=text,lang='es')
        tts.save(word_file_path)
        time.sleep(0.1)
        playsound(word_file_path, block=True)
