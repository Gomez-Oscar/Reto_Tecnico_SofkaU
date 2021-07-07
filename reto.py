import random

class Car():
    def __init__(self, driver, track, lane, distance, finish):
        self.driver = driver
        self.track = track
        self.lane = lane
        self.distance = distance
        self.finish = finish # para saber si el carro ya termino

def dice():
    return random.randint(1, 6)

# se guardan los nombres de los ganadores de todas las carreras en la partida actual
totalDrivers = []  
newGame = True

print('\nBienvenido al Juego de Carros.')

while True:

    try:
        start = int(input('\nPara continuar presione 1\nPara salir presione 0\n: '))

        if start < 0 or start > 1:
            print('\nIngresa el número 1 o 0\n')
            continue
        elif start == 0:
            print('\nGracias por jugar\n')
            break
        else:
            while True:
                try:
                    print('\nIngrese el número de la pista:')
                    print('pista 1: 3 Km (3 carriles)')
                    print('pista 2: 4 Km (4 carriles)')
                    print('pista 3: 5 Km (5 carriles)')
                    track = int(input(': '))

                    if track > 3 or track < 1: 
                        print('\nIngresa un número del 1 al 3\n')
                        continue
                    else:
                        break
                except ValueError:
                    print('\nValor Incorrecto')
                    print('Ingresa un número del 1 al 3\n')

            driversNumber = track + 2
            trackLimit = (track + 2) * 1000
            carsArray = []
            positions = [] # se guardan los nombres de los ganadores de cada carrera
            counter = 0

            # se crean los objetos Car 
            for i in range(driversNumber):
                print("Ingrese el nombre del conductor ", (i + 1))
                myCar = Car(input(), track, i, 0, False)
                carsArray.append(myCar)

            # se itera cada objeto y se aumenta su distancia aleatoriamente con la función dice()
            while counter != driversNumber:
                for i in range(len(carsArray)):
                    if not(carsArray[i].finish): carsArray[i].distance += dice() * 100
                    print(carsArray[i].driver, carsArray[i].distance,'m')
                    if i + 1 == len(carsArray): print('********************')
                    if carsArray[i].distance > trackLimit and not(carsArray[i].finish):
                        carsArray[i].finish = True
                        positions.append(carsArray[i].driver)
                        totalDrivers.append(carsArray[i].driver)
                        counter += 1 # cuenta el número de carros que han finalizado

            print('\nPODIO:')
            for i in range(len(positions)):
                print('posicion',i+1,':', positions[i])
                if i + 1 == 3: break

            f = open ('database.txt','a')
            if newGame: 
                f.write('NUEVO JUEGO\n')
                newGame = False
            f.write('PODIO:\n')

            # victorias es el número de veces que un conductor ha alcanzado podio 
            # en distintas carreras en una partida
            for i in range(len(positions)):
                f.write(f'Posicion {i+1}: ')
                f.write(positions[i])
                f.write(', Victorias: ')
                f.write(f'{totalDrivers.count(positions[i])}')
                f.write('\n')
                if i + 1 == 3: break

            f.write('********************************\n')
            f.close()

    except ValueError:
        print('\nValor Incorrecto, ingresa 1 o 0')



