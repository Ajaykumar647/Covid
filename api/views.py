from django.shortcuts import render
from .models import HospitalModel
from .serializers import HospitalSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def product_list(request):
    if request.method =='GET':
        hospitalname = request.GET.get('hospital_name',"")
        situation = request.GET.get('critical_level',"")
        pincode = request.GET.get('pin_code',"")
        
        dateslot = request.GET.get('date_slot',"")
        
        hospital_list=[]
        covid_data = list(HospitalModel.objects.filter(hospital_name=hospitalname,critical_level=situation,
        pin_code=pincode,date_slot=dateslot))
        
        for i in covid_data:
            data = {
                "hospital_name" : i.hospital_name,
                "critical_level" : i.critical_level, 
                "pin_code" : i.pin_code,
                "date_slot" : i.date_slot,
                "time_slot" : i.time_slot,  
                "beds" : i.beds, 
                  }
            hospital_list.append(data)
        return Response(status=status.HTTP_200_OK,
                        data={'data':hospital_list,'success': True})
        
    elif(request.method =='POST'):
        serializers=HospitalSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_data(request):
    hospital_list = HospitalModel.objects.values()
    final_list = []
    for i in hospital_list:
        data = {
                "id"  : i['id'],
                "hospital_name" : i['hospital_name'],
                "critical_level" : i['critical_level'], 
                "pin_code" : i['pin_code'],
                "date_slot":i['date_slot'],
                "time_slot" : i['time_slot'],  
                "beds" : i['beds'], 
                   
               }
        final_list.append(data)
    return Response(status=status.HTTP_200_OK,
                                     data={'data':final_list,'success': True})


@api_view(["POST"])
def edit_date(request):
    try:
         
        date_obj = HospitalModel.objects.get(id=request.data['booking_id'])
        if 'date_slot' in request.data:
            date_obj.date_slot = request.data['date_slot']
      
        date_obj.save()
        return Response(status=status.HTTP_200_OK,
                        data={'message':'Successfully Updated','success': True})
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": str(e), "success": False})

@api_view(["POST"])
def cancel(request):
    try:
        HospitalModel.objects.filter(id=request.data['booking_id']).delete()
        return Response(status=status.HTTP_200_OK,
                        data={'message':'Successfully Deleted','success': True})
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": str(e), "success": False})


