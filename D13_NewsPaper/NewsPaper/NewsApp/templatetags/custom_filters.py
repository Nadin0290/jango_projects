from django import template

register = template.Library()

@register.filter(name='Censor')
def Censor(text):
    text = str(text).lower().split(' ')
    forbidden_words = [
    'мразь','гнилой','пожилой','каворкинг','бомж'
    ]
    edited_text = ''
    for word in text:
        if word in forbidden_words:
            last_letter = len(word)-1
            first_letter = 0
            for i in range(len(word)):
                if i == first_letter:
                    edited_text += word[first_letter]
                    continue
                elif i == last_letter:
                    edited_text += word[last_letter]
                    edited_text += ' '
                    continue
                edited_text += '*'
        else:
            edited_text += word + ' '

    return str(edited_text)

@register.filter(name='MyType')
def Type(text):
    type = str(text)
    if type.isalpha():
        if str(text) == 'AR':
            return 'Article'
        else:
            return 'New'
    else:
        return None
