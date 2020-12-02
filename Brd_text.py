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

rand_writed_text = open('randtext.txt', 'wt', encoding='utf-8')
rand_writed_text.write(randtext)



