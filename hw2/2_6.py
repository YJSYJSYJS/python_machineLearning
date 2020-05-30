# 거북이가 가는 게임을 만드는 클래스 생성
# 게임 하나 인스턴스를 생성
# (0,0)에서 출발 스피드만큼 칸 이동

class Turtle:
    def __init__(self):
        self.x, self.y, self.direction, self.speed = 0,0,0,1

    def east(self):
        self.direction = 0 # (self.speed, 0)
    
    def west(self):
        self.direction = 1 # (-self.speed, 0)

    def south(self):
        self.direction = 2 # (0, self.speed)

    def north(self):
        self.direction = 3 # (0, -self.speed)
    
    def acceleration(self):
        if self.speed<3:
            self.speed += 1
        
    def brake(self):
        if self.speed>0:
            self.speed -= 1
        
    def printposition(self):
        if self.direction == 0:
            self.x += self.speed
        elif self.direction == 1:
            self.x -= self.speed
        elif self.direction == 2:
            self.y -= self.speed
        elif self.direction == 3:
            self.y += self.speed
        else:
            print('방향이 이상합니다, 방향을 동쪽으로 재설정 하겠습니다.')
            self.direction = 0
        print('지금 위치는 ({}, {})입니다.'.format(self.x, self.y))
        
    def finish(self):
        print('({}, {})에서 끝납니다.'.format(self.x, self.y))

t = Turtle()
t.south()
t.printposition()
t.acceleration()
t.printposition()
t.west()
t.printposition()
t.finish()