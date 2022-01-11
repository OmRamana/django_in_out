from vpic import TypedClient

c = TypedClient()
result = c.decode_vin("1FA6P8TD5M5100001", 2021)


def get_vin_details():
    attributes= []
    attributes.append(result.model_year)
    attributes.append(result.vehicle_type)
    attributes.append(result.make)
    attributes.append(result.model)
    attributes.append(result.series)
    attributes.append(result.trim)
    attributes.append(result.fuel_type_primary)
    attributes.append(result.transmission_style)
    attributes.append(result.drive_type)
    return attributes
    