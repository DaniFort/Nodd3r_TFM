import os
BASE_PATH = 'AumentedData'
SPLITS = {
    'train':0.75,
    'validation':0.15,
    'test':0.10
    }
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',  'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'del','space']
for letter in LETTERS:
    for i in ['train','validation','test']:
        path = os.path.join(BASE_PATH,i,letter)
        print(letter,i,': ',len(os.listdir(path)))