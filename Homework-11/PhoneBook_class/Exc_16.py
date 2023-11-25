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

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None
    

    def remove_contacts(self, id):
        for dict_ in [x for x in self.contacts if x['id'] == id]:
            self.contacts.remove(dict_)
        # for d in self.contacts:
        #     if d['id'] == id:
        #         self.contacts.remove(d)
        return f'Contact successfully removed from addressbook'        
                




# option_ch = Contacts()
# option_ch.add_contacts('Wylie Pope', '(692) 802-2949',
#                        'est@utquamvel.net', False)
# option_ch.add_contacts('Cyrus Jackson', '(501) 472-5218',
#                        'nibh@semsempererat.com', False)
# option_ch.add_contacts('Figli Tamm', '(641) 321-2780', 'figli@sver.io', False)

# print(option_ch.get_contact_by_id(1))

add_var = Contacts()
add_var.add_contacts('Some Person', '(123) 456-1789', 'some@email.com', False)


#print((Contacts.contacts))

print(add_var.get_contact_by_id(1))

print(add_var.remove_contacts(1))