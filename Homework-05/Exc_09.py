def formatted_numbers():
    a = 15
    list = ['|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary')]
    for num in range(a + 1):
        int(num)
        dec = '{:d}'.format(num)
        hex = '{:x}'.format(num)
        bin = '{:b}'.format(num)
        list.append('|{:<10}|{:^10}|{:>10}|'.format(dec, hex, bin))
    return list

for el in formatted_numbers():
    print(el)



# for i in range(16):
#     #s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     dec = "{:d}".format(i)
#     hex = "{:x}".format(i)
#     bin = "{:b}".format(i)
#     s = "|{:<10}|{:^10}|{:>10}|".format(dec, hex, bin)
#     print(s)