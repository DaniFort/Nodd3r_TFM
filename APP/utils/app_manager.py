#text things
full_registered_text = ''
writed_text = ''
writed_text = 'aqui se escribira el texto que el usuario vaya escribiendo con sus manos aplicando símbolos con las manos'

def get_writed_text():
    global writed_text
    return writed_text

def add_update_to_writed_text(text:str):
    global writed_text
    global full_registered_text
    if text == 'space':
        writed_text+=' '
        full_registered_text+= ' '
    elif text == 'del':
        writed_text = writed_text[:-1]
        full_registered_text = full_registered_text[:-1]
    else:
        writed_text+=text
        full_registered_text+= text
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


