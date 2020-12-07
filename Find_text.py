#--------------------------------------
# Поиск в тексте 
# 
# Viktor 06.12.20
# v 1.0
#--------------------------------------
#----------update----------------------
# диалоговое окно для поиска конкретного слова и просмотр предложения, где оно встречается.

import re

def find_word(word, text):
    """
    получает слово и выводит колличество данных совпадений в тексте
    """
    the_word = re.findall(word, text)
    length = len(the_word)
    print('В тексте {} слов "{}" '.format(length, word))

text = open('maintext.txt', 'rt', encoding='utf-8')
text_read = text.read()
while True:
    message = input('\t искомое слово, или "exit" для выхода   ')
    if message == 'exit':
        break
    find_word(message, text_read)

print('game over')
