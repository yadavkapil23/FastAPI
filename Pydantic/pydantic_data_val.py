from pydantic import BaseModel,EmailStr,AnyUrl,Field

#data validation refers to the process of checking that input data conforms to the expected types, formats, and constraints
from typing import List,Dict,Optional,Annotated

#EmailStr is a special type provided by Pydantic to validate that a string is a valid email address.
#AnyUrl is a base type used for validating and representing URLs
#A field in Pydantic is any attribute (like name, age, etc.) inside a Pydantic model , sometimes you want to add extra information or rules to a field—like a default value, a description, or a minimum value. That’s where the Field() function comes in.


class Patient(BaseModel):
    first_name : str = Field(max_length=24)
    last_name : Annotated[str, Field(max_length=50,title="Name of the Patient",description="Give the name of patient in less than 50 characters.",examples=['Kumar','Singh'])]
    age : int = Field(ge=18,lt=58)
    sex : str = "Male" 
    linkedin_url : AnyUrl
    email : EmailStr
    height : float = Field(gt=5,lt=7) #here we are using field function to set the height to min of 5 foot and max of 7 foot.
    married : bool = False #here also we can set the default value.
    allergies : Optional[List[str]] = None #if we want to make this optional  , we have to give this a default value , like None.
    contact_details : dict[str,str]

patient_details = {'first_name' : 'kapil','age' : 20,'sex' : 'male','email' : 'xyz@xmail.com','linkedin_url': 'http://linkedin.com/kapil_yadav','height':6.1,'married': False,'allergies' : ['flowers','chocolates','monkeys'],'contact_details': {'mobile' : '1234567890'}}

patient_1 = Patient(**patient_details)

def details_insertion(patient : Patient):
    print(patient.first_name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.sex)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

details_insertion(patient_1)