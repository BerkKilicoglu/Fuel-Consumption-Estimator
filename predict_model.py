import joblib

model = joblib.load('trained_ml_model.pkl')

"""
**brand**             **orgin**
0- Amc                1- ABD
1- Audi               2- Avrupa
2- Bmw                3- Japonya
3- Buick
4- Cadillac
5- Capri
6- Chevrolet
7- Chrysler
8- Datsun
9- Dodge
10- Fiat
11- Ford
12- Harvester
13- Honda
14- Mazda
15- Mercedes
16- Mercury
17- Nissan
18- Oldsmobile
19- Opel
20- Peugeot
21- Plymouth
22- Pontiac
23- Renault
24- Saab
25- Subaru
26- Toyota
27- Triumph
28- Volkswagen
29- Volvo
"""
def PredictPerGalon(cylinders, displacement, horsepower, weight, acceleration,
                     modelyear, origin, brand):
    


    mil_per_galon = [
        cylinders,
        displacement,
        horsepower,
        weight,
        acceleration,
        modelyear,
        origin,
        brand
        ]
    
    miles_per_galon = [
    mil_per_galon
    ]
    
    predicted_galon_values = model.predict(miles_per_galon)
    
    predicted_galon = predicted_galon_values[0]
    
    return predicted_galon

