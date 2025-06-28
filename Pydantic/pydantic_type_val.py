# from pydantic import BaseModel

# class Patient(BaseModel):  #class bnayi h Basemodel use krke.
#     name : str
#     age : int


# def inser_patient_data(patient : Patient):  #function h data insertion ka.
#     print(patient.name)
#     print(patient.age)
#     print("data inserted successfully.")


# patient_info = {'name' : 'kapil','age' : 19}  #details store krne k liye dictionary h.
# patient_details = {'name' : 'sahil','age' : 45}

# patient_1 = Patient(**patient_info) #patient1 object bnaya h Patient class ka , or uske andar dictionary ko unfold krke daal diya h.



# def update_patient_details(patient : Patient):
#     print(patient.name)
#     print(patient.age)
#     print("details updated.")


# patient_updated = Patient(**patient_details)


# inser_patient_data(patient_1) #function ko call kr diya , patient_1 ka data daal kr.

# update_patient_details(patient_updated)


























from pydantic import BaseModel
from typing import List,Dict,Optional

class Patient(BaseModel):
    name : str
    age : int
    sex : str
    height : float
    married : bool = False #here also we can set the default value 
    allergies : Optional[List[str]] = None #if we want to make this optional  , we have to give this a default value , like None.
    contact_details : dict[str,str]

patient_details = {'name' : 'kapil','age' : 20,'sex' : 'male','height':6.1,'married': False,'allergies' : ['flowers','chocolates','monkeys'],'contact_details': {'email' : 'kapil@gmail.com','mobile' : '1234567890'}}

patient_1 = Patient(**patient_details)

def details_insertion(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.sex)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

details_insertion(patient_1)