import time

class TrafficLight:
    __color = 'фиолетовый'

    def running(self):
        while True:
            print('Горит красный')
            time.sleep(7)
            print('Горит желтый')
            time.sleep(2)
            print('Горит зеленый')
            time.sleep(7)
            print('Горит желтый')
            time.sleep(2)

trafficlight = TrafficLight()
trafficlight.running()