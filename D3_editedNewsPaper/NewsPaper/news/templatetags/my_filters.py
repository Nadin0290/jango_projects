from django import template
 
register = template.Library()

@register.filter(name='Censor')

def Censor(value):
    if isinstance(value, str):
        small_text = value.lower()
        edited_text = small_text.replace(',','')
        text = edited_text.split(' ') 
        bad_words = [ 'падонок', 'убийца','мразь','алкаш','убил']

        for i in range(length(text)):
            bad_word = text[i]

            for word in bad_words:
                if bad_word == word:
                    text[i] = '*****'
                    
    return To_string(text)


def To_string(value):
    my_text = ''
    for element in value:
        my_text += element
        my_text += ' ' 
    return my_text

def length(text):
    counter = 0
    for element in text:
        counter += 1
    return counter
