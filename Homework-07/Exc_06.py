def solve_riddle(riddle: str, word_length, start_letter, reverse=False):
    word = ''
    if reverse == False:
        word = riddle[riddle.find(start_letter):riddle.find(start_letter)+word_length:]
        if word != 0:
            return word
        return word
    elif reverse == True:
        riddle_r = riddle[::-1]
        print(riddle_r)
        word = riddle_r[riddle_r.find(start_letter):riddle_r.find(start_letter)+word_length:]
        if word != 0:
            return word
        return word

s = 'terpower1im'
s_r = "mi1rewopret"

# print(s.find('p'))

# word = s[s.find('p'):s.find('p')+5:1]
# print(word)
s_r_n = 'mi1powperet'
print(solve_riddle(s,5,'p'))
print(solve_riddle(s_r,5,'p', True))
print(solve_riddle(s_r_n, 3, 'r', True))