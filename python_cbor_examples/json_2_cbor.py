import cbor2

# Encode to CBOR
data = {
    "id": 123,
    "name": "Temperature Sensor",
    "value": 25.5,
    "active": True
}

# Encode to CBOR
cbor_data = cbor2.dumps(data)
print("CBOR (Hex):", cbor_data.hex())

# Decode from CBOR
decoded = cbor2.loads(cbor_data)
print("\n\n\n Decoded:", decoded)
    
# Save as a binary file
with open("sensor_data.cbor", "wb") as f:
    cbor2.dump(data, f)
    
# Read from the binary file
with open("sensor_data.cbor", "rb") as f:
    loaded_data = cbor2.load(f)

print("Original Data:", data)
print("Loaded Data:", loaded_data)
assert data == loaded_data  # Verify integrity