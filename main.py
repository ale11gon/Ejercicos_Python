import pickle

class Vehículo:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

coche = Vehículo('seat','rojo')

f = open('datos.obj','wb')
pickle.dump(coche,f)
f.close()

f = open('datos.obj','rb')
pickle.load(f)
f.close()
