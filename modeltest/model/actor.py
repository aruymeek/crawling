class ActorModel:
    movie_key = ''
    name = ''
    age = 0

    def __init__(self, _key, _name, _age):
        self.movie_key = _key
        self.name = _name
        self.age = _age

    def ShowActorInfo(self):
        print('Movie Key: {0}, Name: {1}, Age: {2}'
        .format(self.movie_key, self.name, self.age))

    def Hello(self):
        print('안녕하세요. {0}입니다.'.format(self.name))