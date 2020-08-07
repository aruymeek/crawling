############### 객체와 클래스 ###############
# 클래스 정의
class Dog:

    #클래스 안에서만 사용되는 변수 (먼저 선언하지 않아도 변수 생성 가능, 클래스에 한해서)
    name = ''
    color = ''
    age = 1

    walk_count = 0

    # __init__: 생성자, Dog라는 클래스가 실행될 때 초기에 만들어지는 부분들
    def __init__(self, _name, _color, _age): #self는 클래스에 접근하는 접두사라고 생각하기 (값을 받지 않는다)
        self.name = _name                    #self.name: 클래스 내의 name이라는 변수를 사용하겠다!
        self.color = _color                  #self.color: 클래스 내의 color라는 변수를 사용하겠다!
        self.age = _age                      #self.age: 클래스 내의 age라는 변수를 사용하겠다!

    #클래스 객체에만 적용되는 함수를 정의할 수 있다
    def ShowName(self):                      #받는 매개변수가 필요하지 않을 때에는 self만
        print('Name: {0} / Color: {1} / Age: {2}'.format(self.name, self.color, self.age))

    def GetColor(self):
        print(self.color)

    def ReName(self, new_name):              #매개변수가 필요할 때에는 self 뒤에!
        self.name = new_name

    def GoWalk(self):
        self.walk_count += 1


# 객체 생성
dog1 = Dog('coco', 'black', 3)            #self에는 매개변수 값을 지정하지 않는다, name = coco, color = black, age = 3
dog1.ShowName()                        
#dog1.GetColor()                      
#print(dog1.age)
#print('Name: {0} / Color: {1} / Age: {2}'.format(dog1.name, dog1.color, dog1.age))

dog1.ReName('cookie')
dog1.ShowName()

dog1.GoWalk()
print(dog1.walk_count)


dog2 = Dog('happy', 'white', 5)          #name = happy, color = white, age = 5
dog2.ShowName()
#dog2.GetColor()
#print(dog2.age)
#print('Name: {0} / Color: {1} / Age: {2}'.format(dog2.name, dog2.color, dog2.age))

dog2.GoWalk()
dog2.GoWalk()
print(dog2.walk_count)


