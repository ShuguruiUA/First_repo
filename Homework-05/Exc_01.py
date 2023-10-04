def real_len(text):
    if text.find("\n"):
        text = text.replace("\n", "")
    if text.find("\t"):
        text = text.replace("\t", "")
    if text.find("\f"):
        text = text.replace("\f", "")
    if text.find("\v"):
        text = text.replace("\v", "")
    if text.find("\r"):
        text = text.replace("\r", "")
    return len(text)

#alternative:

def real_len(text):
    char_count = 0
    for char in text:
        if char not in ['\n', '\f', '\r', '\t', '\v']:
            char_count += 1
    return char_count