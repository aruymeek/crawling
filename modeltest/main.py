############### 모델 Model ###############
### 클래스 불러오기
from model.movie import MovieModel


### 클래스를 통해서 리스트에 값 집어넣기 (=모델화)
# ★★★★★ 여기 이해하는 것이 중요 ★★★★★
movies = []

#첫번째 영화 추가
AboutTime = MovieModel('MOV001', '어바웃 타임', 2013, '영국')
AboutTime.AddActor('레이첼 맥아담스', 43)   #영화에 직접 배우를 추가
AboutTime.AddActor('도널 글리슨', 38)
#AboutTime.actors.append(ActorModel(AboutTime.movie_key, '도널 글리슨', 38)) 이 방법도 가능! 
#단, 이렇게 하려면 ActorModel을 import 해야함
movies.append(AboutTime)
AboutTime.AddDirector('리차드 커티스')

#두번째 영화 추가
Parasite = MovieModel('MOV002', '기생충', 2019, '한국')
Parasite.AddActor('최우식', 31)
movies.append(Parasite)
Parasite.AddDirector('봉준호')
#Parasite.directors.append(DirectorModel(Parasite.movie_key, '봉준호')) 이렇게도 가능!
#단, 이렇게 하려면 DirectorModel을 import 해야함

#세번째 영화 추가
Avengers4 = MovieModel('MOV003', '어벤져스: 엔드게임', 2019, '미국')
Avengers4.AddActor('로버트 다우니 주니어', 56)
Avengers4.AddActor('크리스 에반스', 40)
Avengers4.AddActor('크리스 헴스워스', 38)
Avengers4.AddDirector('앤소니 루소')
Avengers4.AddDirector('조 루소')
movies.append(Avengers4)


### for문을 이용하여 값 출력하기
#print(movies)     #엥? list형태로 []가 출력되긴 했지만 안에 값이 이상하네? --> 클래스 형태로 집어넣었기 때문
#print(movies[0].title) #이렇게는 출력할 수 있지, movies[0] = '어바웃 타임' 정보들

for movie in movies:
    print('{0} {1} {2}'.format(movie.title, movie.nation, movie.year))

    for director in movie.directors:
        print('    - 감독: {0}'.format(director.name))

    for actor in movie.actors:
        print('    - {0} {1}'.format(actor.name, actor.age))


#for movie in movies:  #movie: 인스턴스(객체) 하나 / movies는 클래스 객체들로 이루어진 리스트(모델)이기 때문
#    movie.ShowMovieInfo()

#    # '등록된 배우 수' 바로 밑에 ShowActorInfo 가 나오게 하려면 어떻게 해야할까?
#    for actor in movie.actors:
#        actor.ShowActorInfo()

#    # '등록된 감독 수' 바로 밑에 ShowDirectorInfo 가 나오게 하려면 어떻게 해야할까?
#    for director in movie.directors:
#        director.ShowDirectorInfo()