from gtts import gTTS
import pygame
import os
import sys

def get_resource_path(relative_path):
    #Obtiene la ruta correcta de los recursos empaquetados en el .exe.
    try:
        base_path = sys._MEIPASS
    except Exception:

        base_path = os.path.abspath(".")
    print(os.path.join(base_path, relative_path))
    return os.path.join(base_path, relative_path)

char_added_path = "APP/Files/Sounds/write_sound.wav"
char_deleted_path = "APP/Files/Sounds/delete_sound.wav"
space_added_path = "APP/Files/Sounds/space_sound.wav"
word_file_path = "APP/Files/Sounds/voice_sound.wav"

class SoundPlayer():
    def __init__(self):
        pygame.mixer.init()

    def play_char_added_sound(self):
        sound = pygame.mixer.Sound(get_resource_path(char_added_path))
        sound.play()

    def play_char_deleted_sound(self):
        sound = pygame.mixer.Sound(get_resource_path(char_deleted_path))
        sound.play()

    def play_space_added_sound(self):
        sound = pygame.mixer.Sound(get_resource_path(space_added_path))
        sound.play()
    def play_text_sound(self,text:str):
        tts = gTTS(text=text,lang='es')
        tts.save(get_resource_path(word_file_path))
        sound = pygame.mixer.Sound(get_resource_path(word_file_path))
        sound.play()
