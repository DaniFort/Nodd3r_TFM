from ui.elements.text_field import TextField
from utils.app_manager import get_writed_text,add_update_to_writed_text,rewrite_writed_text
from utils.image_flow import get_frame_info,update_frame
from utils import time_control

import cv2

import random

class PartialText():
    def __init__(self, max_per_line = 42):
        self.len = 0
        self.text = ''
        if max_per_line >=15:
            self.max_per_line = max_per_line
        else:
            self.max_char_per_line = 15    
    def add_word(self,word):
        if self.len + len(word) <= self.max_per_line:
            self.len += len(word)+1
            self.text+=word+' '
            return self.text
        else:
            return None  
class WritedTextField(TextField):
              
    def __init__(self, point:tuple,font_face = cv2.FONT_HERSHEY_PLAIN, color = (255,0,0),font_scale = 2,thickness=2,line_spacing = 10,max_char_per_line=34):
        super().__init__('', point,font_face, color ,font_scale,thickness,line_spacing)
        if max_char_per_line >=15:
            self.max_char_per_line = max_char_per_line
        else:
            self.max_char_per_line = 15
            print('Warning: Text must contain minimum 15 characters')
        self.second_is_full = False
        self.cursor_time = 0.5
        self.cursor_timer = 0
        self.show_cursor = True
        
    
    def start(self):
        super().start()
        pass


    def split_text(self):
        parts = get_writed_text().split(' ')
        self.t1 = PartialText(max_per_line=self.max_char_per_line)
        self.t2 = PartialText(max_per_line=self.max_char_per_line)
        for i in range(len(parts)):
            added = self.t1.add_word(parts[0])
            if added == None:
                break
            parts.pop(0)
        for i in range(len(parts)):
            added = self.t2.add_word(parts[0])
            if added == None: #las dos linias estan llenas
                self.go_next_line()
                self.split_text()
                break
            parts.pop(0)

    def go_next_line(self):
        new_text = get_writed_text()
        new_text = new_text.replace(self.t1.text, '')
        rewrite_writed_text(new_text)

    def update(self):
        self.split_text()
        self.cursor_timer += time_control.deltatime
        if self.cursor_timer >=self.cursor_time:
            self.show_cursor = not self.show_cursor
            self.cursor_timer = 0

    

    def draw(self):
        super().draw()
        if self.show_cursor:
            if self.t2.len>0:
                self.t2.text = self.t2.text[:-1]+'|'
            else:
                self.t1.text = self.t1.text[:-1]+'|'

        img = cv2.putText(
            img=get_frame_info(),
            text = self.t1.text,
            org=self.point,
            fontFace=self.font_face,
            color = self.color,
            fontScale= self.font_scale,
            thickness= self.thickness,
        )
        # update_frame(img)

        img = cv2.putText(
            img=img,
            text = self.t2.text,
            org=(self.point[0],self.point[1]+self.line_spacing),
            fontFace=self.font_face,
            color = self.color,
            fontScale= self.font_scale,
            thickness= self.thickness,
        )

        update_frame(img)

