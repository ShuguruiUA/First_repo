import re

text = 'Some text, tExt, tEXT, TeXT'
spam_words = ['text']
# for word in spam_words:
#     search_var = re.findall(word,text,re.IGNORECASE)
#     print(search_var)

def replace_spam_words(text, spam_words):
    #pattern = 
    for word in spam_words:
        search_var = re.findall(word,text,re.IGNORECASE)
        for el in search_var:
            replace_var = re.sub(el, r'\*'*len(el),text,flag=re.IGNORECASE)
            return replace_var
    return text
    
            

