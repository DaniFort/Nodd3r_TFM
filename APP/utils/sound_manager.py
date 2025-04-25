from gtts import gTTS
from playsound import playsound

char_added_path=''
char_deleted_path=''
space_added_path=''
word_file_path=''

class SoundPlayer():
    def play_char_added_sound(self):
        playsound(char_added_path,block=False)
    def play_char_deleted_sound(self):
        playsound(char_deleted_path)
    def play_space_added_sound(self):
        playsound(space_added_path)
    
    def play_text_sound(self,text:str):
        tts = gTTS(text=text,lang='es')
        tts.save(word_file_path)
        playsound(word_file_path, block=False)