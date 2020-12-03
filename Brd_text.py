#--------------------------------------
# Работа с текстовым файлом 
# 
# Viktor 30.11.20
# v 1.01 02.12.20
#--------------------------------------
#----------update----------------------
# кинуть randtext в игнор как и maintext
# 


import random
import re

maintext = open('maintext.txt', 'rt', encoding='utf-8')
text = maintext.read() 


# разбить текст на логические отрезки
array_words = text.split(' ') # на слова
array_sentence = text.split('.') # на предложения

# узнать кол во элементов в тексте
text_len = len(text) # кол во символов
array_words_len = len(array_words) # кол во слов
array_sentence_len = len(array_sentence) # кол во предложений

print('В тексте содержится: {} символов,  {} слов, {} предложений'.format(text_len, array_words_len, array_sentence_len))

#случайно перемешанный текст
shuffle_text = array_words.copy()  # копировать
random.shuffle(shuffle_text) # перемешать
randtext = ' '.join(shuffle_text) # преобразовать в текст

iterator_list = len(array_words)
i = 0
for word in array_words:
    find = re.sub('\n', ' ', word )
    array_words[i] = find 
    i +=1

text = ' '.join(shuffle_text) # преобразовать в текст
count = 0
i=0
k=0
new_text = ''
for w in text:
    if w == ' ' or w == '  ' or w == ', ':
        count +=1
    if count == 8:
        w = '\n'
        count = 0
        new_text += text[k:i]
        new_text+=w
        k=i
        print(new_text)
    i+=1
# запись текста 
rand_writed_text = open('randtext.txt', 'wt', encoding='utf-8') 
rand_writed_text.write(randtext)# случайный текст





