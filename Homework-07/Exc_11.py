def sequence_buttons(string: str):
    char_list = ('a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.',',','?','!',':')
    dig_list = ('2', '22', '222', '3', '33', '333', '4','44','444','5','55','555','6','66','666','7','77','777','8','888','9','99','999','9999','1','11','111','1111','11111')
    translate_dict = {}
    for c, d in zip(char_list,dig_list):
        translate_dict[ord(c)] = d
    new_str = ''.join(ch.lower() for ch in string)
    return new_str.replace(' ','0').translate(translate_dict)
    
    
print(sequence_buttons('Hello world!'))   
print(sequence_buttons('Hi there!'))    

"""

Функція sequence_buttons повертає неправильний результат: 444448884433777330. 
Очікувалося, що функція sequence_buttons при отриманні параметра 'Hi there!' поверне наступний список 44444084433777331111
Кнопка	Символи
1	. , ? ! :
2	A B C
3	D E F
4	G H I
5	J K L
6	M N O
7	P Q R S
8	T U V
9	W X Y Z
0	Пробіл
"""
    
#char_list = ('a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.',',','?','!',':',' ')
#dig_list = ('2', '22', '222', '3', '33', '333', '4','44','444','5','55','555','6','66','666','7','77','777','8','888','9','99','999','9999','1','11','111','1111','11111','0')

# char_list = ('a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.',',','?','!',':',' ')
# dig_list = ('2', '22', '222', '3', '33', '333', '4','44','444','5','55','555','6','66','666','7','77','777','8','888','9','99','999','9999','1','11','111','1111','11111','0')
# translate_dict = {}
# for c, d in zip(char_list,dig_list):
#     print(f'{c}:{d}')
    
# print("Hello world!".translate(translate_dict))
# print("Hello world!".lower())
# print("Hello world!".strip())
# print("Hello world!".replace(" ",''))

# CYRILLIC = ("а", "ч", "ш")
# LATIN = ("a", "ch", "sh")

# TRANSLIT_DICT = {}

# for c, l in zip(CYRILLIC, LATIN):
#     TRANSLIT_DICT[ord(c)] = l
#     TRANSLIT_DICT[ord(c.upper())] = l.upper()

# print("чаша".translate(TRANSLIT_DICT))  # chasha
# print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA