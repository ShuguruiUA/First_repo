def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    for word in spam_words:
        if space_around:
            if f' {word} ' in text or text.startswith(word + ' ') or text.endswith(' ' + word) or text.endswith(word + '.'):
                return True
        else:
            if word in text:
                return True
            
    return False

    # new_text = text.lower()
    # new_text = new_text.split(" ")
    # for word in spam_words:
    #     for word_1 in new_text:
    #         if not space_around:
    #             if word_1.find(word):
    #                 return True
    #         return False
       
            
    #return False
       
                    
    # index = 0
    # for new_text in spam_words:
    #     if not space_around:
    #         new_text[index].lower() != spam_words
    #         index += 1
    #         return False
    #     else:
    #         return True
# def is_spam_words(text, spam_words, space_around=False):
#     text_set = set(text.split())
#     sw_set = set(spam_words)
#     if not space_around:
#         if sw_set.intersection(text_set):
#             return True
#         return False


print(is_spam_words('Молох бог ужасен.', ['Лох']))
print(is_spam_words('Молох бог ужасен.', ['лох'], True))
print(is_spam_words('Ты хорош, но выглядишь как лох.', ['лох']))
print(is_spam_words('Ты хорош, но выглядишь как лох.', ['лох'], True))
