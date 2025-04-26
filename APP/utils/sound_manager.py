from gtts import gTTS
import pygame
import os

char_added_path=os.path.join('APP','Files','Sounds','write_sound.wav')
char_deleted_path=os.path.join('APP','Files','Sounds','delete_sound.wav')
space_added_path=os.path.join('APP','Files','Sounds','space_sound.wav')
word_file_path=os.path.join('APP','Files','Sounds','voice_sound.wav')

class SoundPlayer():
    def __init__(self):
        pygame.mixer.init()

    def play_char_added_sound(self):
        sound = pygame.mixer.Sound(char_added_path)
        sound.play()

    def play_char_deleted_sound(self):
        sound = pygame.mixer.Sound(char_deleted_path)
        sound.play()

    def play_space_added_sound(self):
        sound = pygame.mixer.Sound(space_added_path)
        sound.play()
    def play_text_sound(self,text:str):
        tts = gTTS(text=text,lang='es')
        tts.save(word_file_path)
        sound = pygame.mixer.Sound(word_file_path)
        sound.play()
