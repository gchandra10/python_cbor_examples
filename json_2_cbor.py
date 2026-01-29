import json, cbor2, os

with open("temperature.json","r") as f:
    data=json.load(f)

with open("temperature.cbor","wb") as f:
    cbor2.dump(data,f)

json_size=os.path.getsize("temperature.json")
cbor_size=os.path.getsize("temperature.cbor")

print("JSON size (bytes):",json_size)
print("CBOR size (bytes):",cbor_size)
print("Reduction:",round((1-cbor_size/json_size)*100,2),"%")

with open("temperature.cbor","rb") as f:
    decoded=cbor2.load(f)

assert data==decoded
print("Integrity check passed")