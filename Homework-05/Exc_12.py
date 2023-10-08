import re

text = 'Some text, tExt, tEXT, TeXT'
spam_words = ['text']
# for word in spam_words:
#     search_var = re.findall(word,text,re.IGNORECASE)
#     print(search_var)


def replace_spam_words(text, spam_words):
    for word in spam_words:
        print(word)
        search_var = text.replace(word, r'*'*len(word))
        search_var = re.sub(word, r'*'*len(word), text, flags=re.IGNORECASE)
    return search_var
    #     for el in search_var:
    #         replace_var = re.sub(el, r'\*'*len(el), text, flag=re.IGNORECASE)
    #         return replace_var
    # return text


print(replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', [
    'began', 'Python']))
# def replace_spam_words(text, spam_words):
#     pattern = "*"
#     # search_var = re.findall(spam_words,text, re.IGNORECASE)
#     # print(search_var)
#     for word in spam_words:
#         print(type(spam_words))
#         search_var = re.findall(word,text,re.IGNORECASE)
#         print(search_var)
# if el in search_var:
#     replace_text = re.sub(el,pattern*len(el),text)
#     return replace_text
# else:
#     continue
#     for el in search_var:
#         replace_var = re.sub(el,'*'*len(el),text)
#         return replace_var
# return text
