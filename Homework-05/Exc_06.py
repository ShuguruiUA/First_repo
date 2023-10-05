# def is_spam_words(text, spam_words, space_around=False):
#     new_text = text.split(" ")
#     for index in new_text:
#         if not spam_words:
#             new_text[index].lower() != spam_words.lower()
#             index += 1
#         else:
#             return True
def is_spam_words(text, spam_words, space_around=False):
    text_set = set(text.split())
    sw_set = set(spam_words)
    if not space_around:
        if sw_set.intersection(text_set):
            return True
        return False


print(is_spam_words('Молох бог ужасен.', ['Лох']))
print(is_spam_words('Молох бог ужасен.', ['лох'], True))
