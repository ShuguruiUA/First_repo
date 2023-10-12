def is_equal_string(utf8_string, utf16_string):
    # print(utf8_string)
    # print(utf16_string)
    #print(utf8_string.decode('utf-8'))
    #print(utf16_string.decode('utf-16'))
    s_from_utf8 = utf8_string.decode('utf-8')
    s_from_utf16 = utf16_string.decode('utf-16')
    if s_from_utf8 == s_from_utf16:
        return True
    else:
        return False
    