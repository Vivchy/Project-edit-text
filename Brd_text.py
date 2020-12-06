#--------------------------------------
# Работа с текстовым файлом 
# 
# Viktor 30.11.20
# v 1.1 06.12.20 исправление format text
#--------------------------------------
#----------update----------------------
# кинуть randtext в игнор как и maintext
# 


import random
import re
  
def format_text(array, num):
    """ Формат построения текста в файле """
    i = 0
    for word in array:
        find = re.sub('\n', ' ', word )
        array[i] = find 
        i +=1
    text = ' '.join(array)
    k = 0
    
    is_word = True
    new_text = ''
    for t in text:
        if k%num == 0 and k != 0:
            if text[k+1] == ' ':
                t =t+'\n'
            else:
                is_word = False
        elif not is_word:
            if text[k+1] == ' ':
                t =t+'\n'
                is_word = True
         
        # elif k % 80 == 1 and t == ' ':
        #     t =''
        new_text +=t
        k+=1
    return new_text

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
       #ы print(new_text)
    i+=1
# запись текста 
rand_writed_text = open('randtext.txt', 'wt', encoding='utf-8') 
rand_writed_text.write(randtext)# случайный текст

rand_writed_text = open('formattext.txt', 'wt', encoding='utf-8') 
rand_writed_text.write(format_text(array_words, 80))




