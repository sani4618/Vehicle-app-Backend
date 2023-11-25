from django.db import models

# vehiclenum:"", model:"",brand:"",manfyear:"",color:"",ownername:"",address:"",phNum:"",image:""

class VehicleAppModel(models.Model):
    vehiclenum=models.CharField(default="", max_length=50)
    model=models.CharField(default="",max_length=50)
    brand=models.CharField(default="",max_length=50)
    manfyear=models.CharField(default="",max_length=50)
    color=models.CharField(default="",max_length=50)
    ownername=models.CharField(default="",max_length=50)
    address=models.CharField(default="",max_length=50)
    phNum=models.CharField(default="",max_length=50)
    image=models.CharField(default="",max_length=5000)
