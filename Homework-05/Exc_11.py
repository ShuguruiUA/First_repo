import re


def find_all_words(text, word):
    search_var = re.findall(word, text, re.IGNORECASE)
    return search_var
# text = 'Some text, tExt, tEXT, TeXT'
# word = 'text'
# search_var = re.findall(word,text,re.IGNORECASE)

# print(search_var)