def get_favorites(contacts):
    return list(filter(lambda contact: contact['favorite'], contacts))


