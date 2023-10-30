import re


def capital_text(s):
    r_pat = r'\.!\?'
    s = s.split()
    new_s = ''
    for el in s:
        el = el.capitalize()
        print(el)
        new_s += "".join(el)
    for elem in new_s:
        if elem in r_pat:
            print(new_s)
            new_s = new_s.replace(r_pat, r_pat + " ")

    return new_s


print(capital_text('alert. boss! oh'))
