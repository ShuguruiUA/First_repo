CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
CYRILLIC = []
for ch in CYRILLIC_SYMBOLS:
    CYRILLIC.append(ch)

TRANS = {}
for c, l in zip(CYRILLIC, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    translated = name.translate(TRANS)
    return translated.upper()


print(translate("Юрій Попов"))
