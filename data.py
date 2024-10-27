class Contact:
    def __init__(self, name=None, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone}'
    
class Lead:
    def __init__(self, name=None, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone}'
    
contacts = [
    Contact('Alice Brown', None, '1231112223'),
    Contact('Bob Crown', 'bob@crowns.com', None),
    Contact('Carlos Drew', 'carl@drewess.com', '3453334445'),
    Contact('Doug Emerty', None, '4564445556'),
    Contact('Egan Fair', 'eg@fairness.com', '5675556667'),
]

leads = [
    Lead(None, 'kevin@keith.com', None),
    Lead('Lucy', 'lucy@liu.com', '3210001112'),
    Lead('Mary Middle', 'mary@middle.com', '3331112223'),
    Lead(None, None, '4442223334'),
    Lead(None, 'ole@olson.com', None),
]