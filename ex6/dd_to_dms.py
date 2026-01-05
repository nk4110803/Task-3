import json
def dd_to_dms(dd):
    degrees = int(dd)
    minutes = int((dd - degrees) * 60)
    seconds = (dd - degrees - minutes / 60) * 3600
    return degrees, minutes,seconds

with open('coordinates.json', 'r') as file:
    data = json.load(file)
for city, coords in data.items():
    dd_values = coords['dd']
    dms_values = [dd_to_dms(abs(dd)) for dd in dd_values]
    print(f"{city}: coordinates in DMS format:")
    for dms in dms_values:
        print(f"{dms[0]}° {dms[1]}' {dms[2]}''")


