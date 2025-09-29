import pydicom

def serializeDicomValue(v):
    if isinstance(v, pydicom.multival.MultiValue):
        return list(v)
    elif isinstance(v, (pydicom.valuerep.PersonName, pydicom.valuerep.DSfloat, pydicom.valuerep.IS)):
        return str(v)
    elif isinstance(v, bytes):
        return v.decode(errors="ignore")
    else:
        return v #normal datatype