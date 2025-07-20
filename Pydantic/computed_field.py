from pydantic import BaseModel,computed_field
from typing import List,Dict,Optional

class Patient(BaseModel):
    name : str
    age : int
    sex : str
    height : float
    weight : float
    married : bool = False 
    allergies : Optional[List[str]] = None 
    contact_details : dict[str,str]


    @computed_field
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


patient_details = {'name' : 'kapil','age' : 20,'sex' : 'male','height':6.1,'weight' : 83.6 , 'married': False,'allergies' : ['flowers','chocolates','monkeys'],'contact_details': {'email' : 'kapil@gmail.com','mobile' : '1234567890'}}

patient_1 = Patient(**patient_details)

def details_insertion(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.sex)
    print(patient.height)
    print(patient.weight)
    print(patient.calculate_bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

details_insertion(patient_1)