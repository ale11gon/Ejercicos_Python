import time

def main():

    t = time.localtime()
    t_hora = int(time.strftime("%H", t))
    t_min = int(time.strftime("%M", t))
    t_sec = int(time.strftime("%S", t))

    if t_hora >= 19:
        print('Es hora de ir a casa')

    else:
        rest_horas = 18 - t_hora
        rest_min = 60 - t_min
        rest_sec = 60 - t_sec
        print('Aun no te vas a casa, te queda:',rest_horas,'horas',rest_min,'minutos y',rest_sec,'segundos')




if __name__ == '__main__':
    main()