from variables.logic import variables_logic
from ..models import Measurement

def get_measurements():
    mesurements= Measurement.objects.all()
    return mesurements

def get_mesaurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def create_measurement(mea):
    var= variables_logic.get_variable(1)
    measurement = Measurement(variable=var,value=mea["value"])
    measurement.save()
    return measurement