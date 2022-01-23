def bad_words(text):
    text = str(text).lower().split(' ')
    forbidden_words = [
    'мразь','гнилой','пожилой','каворкинг','бомж'
    ]
    edited_text = ''
    #     for word in text:
    #         if word not in List_of_bad_words:
    #             edited_text += word + ' '
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

print(bad_words('Вчера ночью пожилой дед обозвал мужика словом мразь'))