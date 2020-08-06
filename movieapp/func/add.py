# 필요한 변수, 메서드 불러오기
from func.datapack import movies, directors, actors
from func.create import CreateKey
from func.helper import FindMovieKey


# (기능 1) 영화 데이터 입력 (고유번호 자동증가)
def AddMovie():
    mov_key = CreateKey('MOV', movies)
    
    mov_info = input('영화 정보를 입력해주세요. (영화제목, 개봉연도, 제작국가): ')
    words = mov_info.split(',')       #split('구분자'): 구분자를 기준으로 문자열 나누기
    
    movies.setdefault(mov_key, words)
           
    return


# (기능 2) 감독 데이터 입력 (고유번호 자동증가)
def AddDirector():
    dir_key = CreateKey('DIR', directors)
    
    dir_info = input('감독 정보를 입력해주세요. (영화제목, 감독이름): ')
    words = dir_info.split(',')
    mov_title = words[0]
    
    isFound, mov_key = FindMovieKey(mov_title)
    
    if isFound == True:
        words[0] = mov_key
        directors.setdefault(dir_key, words)
        
    else:
        print('▶ 해당 영화 제목(\'{0}\')을 찾을 수 없습니다.'.format(mov_title))
    
    return


# (기능 3) 배우 데이터 입력 (고유번호 자동증가)
def AddActor():
    act_key = CreateKey('ACT', actors)
    
    act_info = input('배우 정보를 입력해주세요. (영화제목, 배우이름, 출생연도): ')
    words = act_info.split(',')
    mov_title = words[0]
    
    isFound, mov_key = FindMovieKey(mov_title)
    
    if isFound == True:
        words[0] = mov_key
        actors.setdefault(act_key, words)
        
    else:
        print('▶ 해당 영화 제목(\'{0}\')을 찾을 수 없습니다.'.format(mov_title))
        
    return