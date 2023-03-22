#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
#Examples
#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    punctuation = ['!', ',', '.', ':', ';', ' ', '?']
    text_new = []
    text = text.split()
    for word in text:
        if word not in punctuation:
            word = word[1::]+word[0]+'ay'
            text_new.append(word)
        else:
            text_new.append(word)
    return ' '.join(text_new)