from django import template

register = template.Library()

@register.filter(name='Censor')
def Censor(text):
    text = str(text).lower().split(' ')
    List_of_bad_words = [
        'мразь','гнилой','пожилой','каворкинг','бомж','изнасиловал'
    ]
    edited_text = ''
    for word in text:
        if word not in List_of_bad_words:
            edited_text += word + ' '

    return str(edited_text)