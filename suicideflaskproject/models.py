from mongoengine import Document
class analyzer(Document):
    id=StringField(max_length=60,required=True,unique=True)
    name=StringField(max_length=60,required=True,unique=True)
    serotonin=FloatField(max_value=283.00,min_value=101.00)
    dopamine = FloatField(max_value=195.80, min_value=120.00)
    glutamate = FloatField(max_value=100.00, min_value=50.00)
    cortisol = FloatField(max_value=23.00, min_value=6.00)
    fivehiaa = FloatField(max_value=36.60, min_value=10.50)
    suicide_percentage=FloatField(max_value=100.00, min_value=0.00)

class register(Document):
    name=StringField(max_length=60,required=True,unique=True)
    email=StringField(max_length=60,required=True,unique=True)
    phno=StringField(max_length=10,required=True,unique=True)
    gender=StringField(max_length=1,required=True,unique=True)
    age=IntegerField(min_val=18,max_val=80,required=True,unique=True)
    pwd=StringField(max_length=60,required=True,unique=True)
