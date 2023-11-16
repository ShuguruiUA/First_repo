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








#'Iurii Popov', '(093)485-01-35', 'popov.yk@gmail.com', favorite=True
some_var = Contacts()
some_var.add_contacts(name='Iurii Popov', phone='0934850135',email='some@email.com',favorite=True)

#some_var.add_contacts(name='Iurii Popov', phone='0934850135',email='some@email.com',favorite=True)
##secont_var=Contacts()
#secont_var.add_contacts(name='Iurii Popov', phone='0934850135',email='some@email.com',favorite=True)
#print(Contacts.list_contacts(some_var))
#print(Contacts.list_contacts(secont_var))


get_con = Contacts()
get_con.get_contact_by_id(id=1)
print(get_con)
