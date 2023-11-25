import re
s = "2+ 34-5 * 3 - 34"
def token_parser(s):
    validate = re.sub(r'\s', '', s)
    lexem = list(re.findall(r'\d+|\D|[^\s]', validate))
    
    return lexem

        
print(token_parser(s))