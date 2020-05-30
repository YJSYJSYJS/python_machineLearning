# 실습과제 5-12(상속클래스)
## 자동차를 나타내는 Car 클래스 구현

class Car:
    max_speed = 160
    speed = 0
    step = 20
    def speed_up(self):
        self.speed+=self.step
        if self.speed>self.max_speed:
            self.speed=self.max_speed
        print("현재 속도: {}".format(self.speed))    

    def speed_down(self):
        self.speed-=self.step
        if self.speed<0:
            self.speed=0
        print("현재 속도: {}".format(self.speed))

# 실습과제 5-13(상속클래스)
## Car 클래스 기반 자식 클래스(SportCar, Truck) 구현

class SportCar(Car):
    max_speed = 200
    step = 45

class Truck(Car):
    max_speed = 100
    step = 15

sc = SportCar()
t = Truck()

sc.speed_up()
sc.speed_down()

t.speed_up()
t.speed_down()


