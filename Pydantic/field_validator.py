from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator

from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : str = Field(max_length=24)
    age : int = Field(ge=18,lt=58)
    sex : str = "Male" 
    linkedin_url : AnyUrl
    email : EmailStr
    height : float = Field(gt=5,lt=7) 
    married : bool = False 
    allergies : Optional[List[str]] = None 
    contact_details : dict[str,str]


    @field_validator('email') #data validation.
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain.")
        return value
        

    @field_validator('name',mode="after") #mode after means , we'll get the value after the type coersion
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode="after")#defaul mode value is always after.
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else: 
         raise ValueError("Please enter a valid age.")


patient_details = {'name' : 'kapil','age' : 20,'sex' : 'male','email' : 'xyz@icici.com','linkedin_url': 'http://linkedin.com/kapil_yadav','height':6.1,'married': False,'allergies' : ['flowers','chocolates','monkeys'],'contact_details': {'mobile' : '1234567890'}}

patient_1 = Patient(**patient_details)  #validation , and also type coersion : automatic conversion of input data into the types defined in a Pydantic model

def details_insertion(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.sex)
    print(patient.height)
    print(patient.married) 
    print(patient.allergies)
    print(patient.contact_details)

details_insertion(patient_1)