import re


def find_word(text, word):
    find_dict = {
        'result' : False,
        'first_index': None,
        'last_index': None,
        'search_string': word,
        'string': text
    }
    search_var = re.search(word, text)
    
    if search_var:
        first_index,second_index = search_var.span()
        find_dict.update({'result': True})
        find_dict.update({'first_index':first_index})
        find_dict.update({'last_index':second_index})
        return find_dict
    else:
        return find_dict
    



print(find_word('something here', 'heare'))