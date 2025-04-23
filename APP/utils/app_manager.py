#text things
writed_text = 'aqui se escribira el te xto\ndq rfw qerfw ejfqf gewga dpjasp fjaspfj apsfjpa sjfasf'
writed_text = 'W'*34

def get_writed_text():
    global writed_text
    return writed_text

def add_update_to_writed_text(text:str):
    global writed_text
    writed_text+=text
    return writed_text

def rewrite_writed_text(text:str):
    global writed_text
    writed_text = text
    return writed_text

# prediction
has_written = False
is_able_to_write = False


def get_is_able_to_write():
    global is_able_to_write
    return is_able_to_write

def set_is_able_to_write(state:bool):
    global is_able_to_write
    global has_written
    is_able_to_write = state
    if state == False and has_written ==True :
        has_written = False



def get_has_written():
    global has_written
    return has_written

def set_has_written(state : bool):
    global has_written
    has_written = state

