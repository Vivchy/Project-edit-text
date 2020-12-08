#--------------------------------------
# Поиск в тексте 
# 
# Viktor 06.12.20
# v 1.0
#--------------------------------------
#----------update----------------------
# диалоговое окно для поиска конкретного слова и просмотр предложения, где оно встречается.

import re
import csv

games = [
    ['1', 'Igor', '12','56'],
    ['2', 'urii', '32', '25'],
    ['3', 'Leonid', '12', '88'],
    ['4', 'Dasha','16', '87']
]
with open('games', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(games)

with open('games', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['id', 'Name', 'age', 'score'])
    games2 = [row for row in cin]
    print(games2)
    
with open('newgame.csv', 'wt') as g:
    cin = csv.DictWriter(g, ['id', 'Name', 'age', 'score'])
    cin.writeheader()
    cin.writerows(games2)

print(c)
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
