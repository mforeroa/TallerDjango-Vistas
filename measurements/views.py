from django.shortcuts import render
from .logic import logic_measurements as ml
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = ml.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            measurement_dto = ml.get_measurements()
            measurements = serializers.serialize('json', measurement_dto)
            return HttpResponse(measurements, 'application/json')
    if request.method == 'POST':
        measurement_dto = ml.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')