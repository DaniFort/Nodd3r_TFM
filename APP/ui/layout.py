class Layout():
    def __init__(self):
        self.elements = []
    
    def add_element(self,element):
        self.elements.append(element)
        return element
    
    def remove_element(self,element):
        self.elements.remove(element)
        return element
    
    def start(self):
        for i in self.elements:
            try:
                i.start()
            except:
                pass    
        # for i in self.elements: #only for test
        #     i.start()
    
    def update(self):
        for i in self.elements:
            try:
                i.update()
            except:
                pass
        # for i in self.elements: #only for test
        #     i.update()

    def draw(self):
        for i in self.elements:
            try:
                i.draw()
            except:
                pass
        # for i in self.elements: #only for test
        #     i.draw()
    
    