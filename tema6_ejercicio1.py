class Vehículo:
    Color = None
    Ruedas = None
    Puertas = None

class Coche(Vehículo):
    Velocidad = None
    Cilindrada = None

ferrari = Coche()
ferrari.Color = 'rojo'
ferrari.Ruedas = 4
ferrari.Puertas = 3
ferrari.Velocidad = 300
ferrari.Cilindrada = 4000

print(ferrari.__dict__)
