text = 'I really really like apples'


def word_count(text):
    text1 = text.replace('.', '')
    text2 = text1.replace(',', '')
    text3 = text2.replace('!', '')
    text4 = text3.replace('?', '')
    lst = text4.split()
    counter = {}

    for word in lst:
        word_counter = counter.get(word)
        if word_counter is None:
            counter[word] = 1
        else:
            counter[word] = word_counter + 1
    return counter

    counter = {item: text.count(word) for items in set(text)}
    print(counter)


print(word_count(text))