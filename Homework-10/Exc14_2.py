class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id: int):
        for contact in self.contacts:
            if contact["id"] == id:
                return contact
        return {}

       
option_ch = Contacts()
option_ch.add_contacts('Wylie Pope', '(692) 802-2949',
                       'est@utquamvel.net', False)
option_ch.add_contacts('Cyrus Jackson', '(501) 472-5218',
                       'nibh@semsempererat.com', False)
option_ch.add_contacts('Figli Tamm', '(641) 321-2780', 'figli@sver.io', False)

#print(str(option_ch.list_contacts()))
print(option_ch.get_contact_by_id()
print(option_ch.get_contact_by_id(3))