def bad_words(text):
    text = str(text).lower().split(' ')
    List_of_bad_words = [
        'мразь','гнилой','пожилой','каворкинг','бомж'
    ]
    edited_text = ''
    for word in text:
        if word not in List_of_bad_words:
            edited_text += word + ' '

    return str(edited_text)

print(bad_words('Вчера ночью пожилой дед обозвал мужика словом мразь'))