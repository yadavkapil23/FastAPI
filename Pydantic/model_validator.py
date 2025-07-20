from pydantic import BaseModel,model_validator
from typing import List,Dict,Optional

class Patient(BaseModel):
    name : str
    age : int
    sex : str
    height : float
    married : bool = False 
    allergies : Optional[List[str]] = None 
    contact_details : dict[str,str]

    @model_validator(mode="after")
    @classmethod
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients greater than 60 years of age should have an emergency contact no.")
        
        return model

patient_details = {'name' : 'kapil','age' : 70,'sex' : 'male','height':6.1,'married': False,'allergies' : ['flowers','chocolates','monkeys'],'contact_details': {'email' : 'kapil@gmail.com','mobile' : '1234567890','emergency':'5678941230'}}

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