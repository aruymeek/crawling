from model.actor import ActorModel
from model.director import DirectorModel

class MovieModel:
    movie_key = ''
    title = ''
    year = 2020
    nation = ''
    # ↑ 얘네도 여기 없어도 됨 ㅎ_ㅎ
    #여기에 actors = [] 구문이 쓰이면, MovieModel 클래스를 쓰는 모든 영화들에 배우 목록이 공유됨 !
    

    def __init__(self, _key, _title, _year, _nation):
        #인스턴스 안 변수들 = 속성
        self.movie_key = _key
        self.title = _title
        self.year = _year
        self.nation = _nation
        self.actors = []     # 영화별로 배우 list를 작성하려면 리스트 선언이 생성자 안에 있어야 함!!!!! ★★★★★
        self.directors = []  # 감독 list도 마찬가지 !!!!! ★★★★★


    def ShowMovieInfo(self):
        print('Movie Key: {0}, Title: {1}, Release: {2}, Nation: {3}'
        .format(self.movie_key, self.title, self.year, self.nation))

        print('등록된 배우 수: {0}'.format(len(self.actors)))

        print('등록된 감독 수: {0}'.format(len(self.directors)))    


    #클래스 내에서 또 다른 클래스(생성자: ActorModel, DirectorModel) 호출하여 사용하기
    def AddActor(self, _name, _age):                      #AddActor에 필요한 변수는 이름과 나이
        # ★★★ 아래 구문 이해하기 ★★★
        actor = ActorModel(self.movie_key, _name, _age)   #self.movie_key는 ActorModel에서 필요한 변수(_key)를 받은 것
        self.actors.append(actor)


    def AddDirector(self, _name):
        director = DirectorModel(self.movie_key, _name)
        self.directors.append(director)


    