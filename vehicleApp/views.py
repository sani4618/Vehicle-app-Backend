from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from vehicleApp.serializers import VehicleAppSerializer
from vehicleApp.models import VehicleAppModel
from django.db.models import Q

# vehiclenum:"", model:"",brand:"",manfyear:"",color:"",ownername:"",address:"",phNum:"",image:""
@csrf_exempt
def DeleteVehicleDetails(request):
    if request.method=="POST":
        received_json_method=json.loads(request.body)
        getVehicleNum=received_json_method["vehiclenum"]
        VehicleAppModel.objects.filter(Q(vehiclenum=getVehicleNum)).delete()
        return HttpResponse(json.dumps({"status":"Deleted Successfully"}))


@csrf_exempt
def SearchVehicleDetails(request):
    if request.method=="POST":  
        received_json_method=json.loads(request.body)
        getBrand=received_json_method["brand"]
        data=list(VehicleAppModel.objects.filter(Q(brand__icontains=getBrand)).values())
        return HttpResponse(json.dumps(data))
    
          

@csrf_exempt
def viewVehicleDetails(request):
    if request.method=="GET":
        vehicleapp_List=VehicleAppModel.objects.all()
        VehicleAppDetailsSerializer=VehicleAppSerializer(vehicleapp_List,many=True)
        return HttpResponse(json.dumps(VehicleAppDetailsSerializer.data))



@csrf_exempt
def RegVehicle(request):
    if request.method=="POST":
        received_json_method=json.loads(request.body)
        getVehicleNum=received_json_method["vehiclenum"]
        getModel=received_json_method["model"]
        getBrand=received_json_method["brand"]
        getManufatureyr=received_json_method["manfyear"]
        getColor=received_json_method["color"]
        getOwnername=received_json_method["ownername"]
        getAddress=received_json_method["address"]
        getPhonenum=received_json_method["phNum"]
        getImage=received_json_method["image"]
        data={"vehiclenum":getVehicleNum,"model":getModel,"brand":getBrand,"manfyear":getManufatureyr,"color":getColor,"ownername":getOwnername,"address":getAddress,"phNum":getPhonenum,"image":getImage}
        print(data)
        VehicleApp_serializer=VehicleAppSerializer(data=data)
        if VehicleApp_serializer.is_valid():
            VehicleApp_serializer.save()
            return HttpResponse(json.dumps({"status":"Sucessfully Registered"}))
        else:
            return HttpResponse(json.dumps({"status":"Adding New vehicle Failed"}))
    else:
        return HttpResponse("invalid")
