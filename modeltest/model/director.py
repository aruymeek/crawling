class DirectorModel:
    movie_key = ''
    name = ''

    def __init__(self, _key, _name):
        #인스턴스 안 변수들 = 속성
        self.movie_key = _key
        self.name = _name

    def ShowDirectorInfo(self):
        print('Movie Key: {0}, Name: {1}'
        .format(self.movie_key, self.name))