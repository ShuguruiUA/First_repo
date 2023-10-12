path = ('output.csv')
def get_credentials_users(path):
    new_list = []
    with open(path, 'rb') as file:
        for line in file:
            #print(line)
            line = line.decode()
            #print(line)
            line = line.replace('\n','')
            #print(line)
            new_list.append(line)
        print(new_list)
        return new_list