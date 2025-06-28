#jb ham kisi ek pydantic model ko kisi dusre pydantic model me as a field use kre , to use nested model bulate hain.
from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str


class Patient(BaseModel):
    name : str 
    age : int
    address : Address


address_dict = {'city':'Gurugram','state': 'Haryana','pin' : '248007'}

address1 = Address(**address_dict)

patient_dict = {'name':'Natasha','age':'19','address':address1}

patient1 = Patient(**patient_dict)

print(address1.pin)
print(patient1.name)
print(patient1.address)

#THE NESTED MODELS ARE USED FOR BETTER ORGANISATION , REUSABILITY , READABILITY , VALIDATION.

#serialisation

temp = patient1.model_dump()

print(temp)
print(type(temp))

x = patient1.model_dump(exclude={'address':['state']})
print(x)