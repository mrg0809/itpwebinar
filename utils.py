from data import contacts, leads, Contact

#registation
def process_registration(registrant, contacts, leads):
    name = registrant['name']
    email = registrant['email']
    phone = registrant['phone']


    #Check email
    for contact in contacts:
        if contact.email == email:
            if contact.phone is None and phone:
                contact.phone = phone
            if contact.name is None and name:
                contact.name = name
            return
    
    #Check phone
    for contact in contacts:
        if contact.phone == phone:
            if contact.email is None and email:
                contact.email = email
            if contact.name is None and name:
                contact.name = name
            return
    
    #Check leads by email
    for lead in leads:
        if lead.email == email:
            leads.remove(lead)
            contacts.append(Contact(name=lead.name or name, email=lead.email, phone=lead.phone or phone))
            return
        
    #Check leads by phone
    for lead in leads:
        if lead.phone == phone:
            leads.remove(lead)
            contacts.append(Contact(name=lead.name or name, email=lead.email or email, phone=lead.phone))
            return
        
    #New contact
    contacts.append(Contact(name=name, email=email, phone=phone))