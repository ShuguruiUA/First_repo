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
        for dict_ in [x for x in self.contacts if x['id'] == id]:
            return dict_
        return None

    # def __repr__(self):
    #     return super().__repr__



# option_ch = Contacts()
# option_ch.add_contacts('Wylie Pope', '(692) 802-2949',
#                        'est@utquamvel.net', False)
# option_ch.add_contacts('Cyrus Jackson', '(501) 472-5218',
#                        'nibh@semsempererat.com', False)
# option_ch.add_contacts('Figli Tamm', '(641) 321-2780', 'figli@sver.io', False)


#'Iurii Popov', '(093)485-01-35', 'popov.yk@gmail.com', favorite=True
# some_var = Contacts()
# some_var.add_contacts(name='Iurii Popov', phone='0934850135',email='some@email.com',favorite=True)
add_var = Contacts()
add_var.add_contacts('Some Person', '(123)456789', 'some@email.com', True)

#some_var.add_contacts(name='Iurii Popov', phone='0934850135',email='some@email.com',favorite=True)
##secont_var=Contacts()
#secont_var.add_contacts(name='Iurii Popov', phone='0934850135',email='some@email.com',favorite=True)
#print(Contacts.list_contacts(some_var))
#print(Contacts.list_contacts(secont_var))


# get_con = Contacts()
# get_con.get_contact_by_id(id=1)
#some_var.get_contact_by_id(id=1)
# print(some_var.get_contact_by_id(id=1))
#print(str(option_ch.list_contacts()))

# print(option_ch.get_contact_by_id(id=2))
print(add_var.get_contact_by_id(1))