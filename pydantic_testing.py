from pydantic import BaseModel,Field,AnyUrl,EmailStr,field_validator,model_validator
from typing import Dict,List,Optional,Literal,Annotated

class Details(BaseModel): #defining a class that inherits frmo BaseModel , making it a Pydantic model.
    first_name : Annotated[str,Field(max_length=24,description="Enter Your Name.",examples=("Rohit","Vipul"))]
    last_name : Optional[str] = None
    aadhar_card : str 
    birth_certificate: Optional[str] = None
    age : int = Field(ge=18 , le=58)
    sex : str 
    married : bool = None
    linkedin_url : AnyUrl
    contact_details : Dict[str,str]
    work_email : EmailStr




#NOW PERFORMING THE FIELD VALIDATION
    @field_validator('linkedin_url')
    @classmethod
    def linkedin_validation(cls,value):
        value_Str = str(value)
        #domain_name = ['http://linkedin.com','https://linkedin.com']
        if "http://linkedin.com" in value_Str or "https://linkedin.com" in value_Str:
            return value
        raise ValueError("Not a LinkedinURL")


#MODEL VALIDATOR 
    @model_validator(mode='after')
    @classmethod
    def aadhar_validation(cls,model):
        if 0 < model.age < 5 and not model.birth_certificate : 
            raise ValueError("Please enter Your Birth Certificate Number.")
        
        return model 













#creating a dictionary to store the information 
information = {'first_name' : 'Kapil','aadhar_card' : '78945625', 'age' : 21 , 'sex': 'male','married' : False,'linkedin_url': 'http://linkedin.com','contact_details' : {'email': 'kapil@gmail.com','phone': '9997845612'},'work_email':'kapil@openai.com'}


#creating a pydantic model instance. , here it unpacks the dictionary information.
person = Details(**information)

def inserting_info(information : Details):
    print(information.first_name)
    print(information.last_name)
    print(information.aadhar_card)
    print(information.age)
    print(information.married)
    print(information.sex)

inserting_info(person)

#HERE DETAILS IS THE MODEL
#HERE INFORMATION IS THE DICTIONARY
#HERE PERSON IS THE INSTANCE OF MODEL.