def parse_folder(path='c:/users'):
    files = []
    folders = []

    for el in path.iterdir():
        if el.is_dir():
            folders.append(el.name)
        else:
            files.append(el.name)

    return files, folders
