message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    # ch = message[i]
    # if ch == " ":
    #     new_ch+= " "
    # elif ch == "!":
    #     new_ch+="!"
    if (ch.isupper()):
        pos = ord(ch) + ord('A')
        pos = (pos + offset) % 26
        new_ch = chr(pos + ord('A'))
    elif (ch.islower()):
        pos = ord(ch) - ord('a')
        pos = (pos + offset) % 26
        new_ch = chr(pos + ord('a'))
    else:
        new_ch = ch
    encoded_message += new_ch
print(encoded_message)
    
# mv = 1
# pos=(ord(ch) - ord(ch))
# print (pos)
# pos=(pos + mv) % 26
# print(pos)
# new_ch = chr(pos + ord("A"))
# print(ord("A"), ord(new_ch))


# for ch in message:
#     if ch == ch.upper():
#         pos = ord(ch) - ord('A')
#         pos = (pos - offset) % 26
#         new_ch = chr(pos + ord('A'))
#     elif ch == ch.lower():
#         pos = ord(ch) - ord('a')
#         pos = (pos - offset) % 26
#         new_ch = chr(pos + ord('a'))
#     else:
#         new_ch = ch
#     encoded_message += new_ch
# print(encoded_message)