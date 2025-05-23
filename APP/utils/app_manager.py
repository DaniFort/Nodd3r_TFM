from utils.sound_manager import SoundPlayer
#text things
full_registered_text = ''
writed_text = ''
max_word_size = 20
sp = SoundPlayer()
def get_writed_text():
    global writed_text
    return writed_text

def add_update_to_writed_text(text:str):
    global sp
    global writed_text
    global full_registered_text

    if text == 'space':
        last_word = writed_text.split(' ')[-1]
        writed_text+=' '
        full_registered_text+= ' '
        sp.play_space_added_sound()
        sp.play_text_sound(last_word)
    elif text == 'del':
        writed_text = writed_text[:-1]
        full_registered_text = full_registered_text[:-1]
        sp.play_char_deleted_sound()
    else:
        if len(writed_text.split(' ')[-1])>= max_word_size:
            text = text+' '
        writed_text+=text
        full_registered_text+= text
        sp.play_char_added_sound()
    return writed_text

def rewrite_writed_text(text:str):
    global writed_text
    global full_registered_text
    writed_text = text
    full_registered_text = text
    return writed_text

# prediction
is_able_to_write = False

def get_is_able_to_write():
    global is_able_to_write
    return is_able_to_write

def set_is_able_to_write(state:bool):
    global is_able_to_write
    global has_written
    is_able_to_write = state


