# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:

ch = "A"
mv = 1
pos=(ord(ch) - ord(ch))
print (pos)
pos=(pos + mv) % 26
print(pos)
new_ch = chr(pos + ord("A"))
print(ord("A"), ord(new_ch))
