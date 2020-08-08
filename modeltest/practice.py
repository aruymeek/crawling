from model.movie import MovieModel
from model.actor import ActorModel
from model.director import DirectorModel


###클래스 객체의 구조 익히기
AboutTime = MovieModel('MOV001', '어바웃 타임', 2013, '영국')
print(type(AboutTime))   # MovieModel이 AboutTime 변수의 type이다. MovieModel은 class.

Rachel = ActorModel('MOV001', '레이첼 맥아담스', 43)
Domhnall = ActorModel('MOV001', '도널 글리슨', 38)

#Rachel, Domhnall은 ActorModel로 만든 변수이니까, ActorModel 내의 Hello 메서드를 쓸 수 있음
Rachel.Hello()
Domhnall.Hello()

AboutTime.actors.append(Rachel)
AboutTime.actors.append(Domhnall)
# AboutTime.actors = [Rachel, Domhnall] 이렇게도 가능~

# AboutTime.AddActor() 메서드를 사용하면 바로 actors 리스트에 추가된다
AboutTime.AddActor('빌 나이', 72)

# <==> AboutTime.directors.append(DirectorModel('MOV001', '리차드 커티스'))
AboutTime.AddDirector('리차드 커티스')


### 클래스의 속성들
print(AboutTime.movie_key)        #어바웃타임 영화 고유 키
print(AboutTime.title)            #어바웃타임 영화 제목
print(AboutTime.year)             #어바웃타임 개봉연도
print(AboutTime.nation)           #어바웃타임 제작 국가
print(AboutTime.actors[0].name)   #어바웃타임 첫번재 배우의 이름
print(AboutTime.actors[1].name)   #어바웃타임 두번째 배우의 이름


### 실행
for actor in AboutTime.actors:
    actor.ShowActorInfo()

for director in AboutTime.directors:
    director.ShowDirectorInfo()