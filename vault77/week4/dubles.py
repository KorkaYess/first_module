
text = 'The quik brown fox jumps over the lazy dog'


def remove_duplicates(text):
    text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    text = text.lower()
    text = text.split()
    print(text)
    new_text = ''

    for word in text:
        if text.count(word) == 1:
            new_text += word + ' '
    return new_text


print(remove_duplicates(text))

