import requests

properties = input("Enter prperties:")
mag = input("Enter mag:")
place = input("Enter place")
res = requests.get(f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-03-01&endtime=2023-03-02&minmagnitude=5")
data = res.json()
features = data['features']
for feature in features:
    print(feature['properties']['mag'], feature['properties']['place'])