from NewsPaper.news.templatetags.my_filters import length, To_string


def bad_boy(value):

    text = value.split(' ') 
    bad_words = [ 'падонок', 'убийца','мразь','алкаш']

    for i in range(length(text)):
        bad_word = text[i]

        for word in bad_words:
            if bad_word == word:
                text[i] == '*'
    return To_string(text)

some_text = 'Убийца программист, который еще и алкаш, убил двух детей под подьездом.'

print(bad_boy(some_text))
        

