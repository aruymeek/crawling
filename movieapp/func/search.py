from func.datapack import movies, directors, actors
from func.helper import GetMovieTitleByMovieKey


# (추가 기능 4) 전체 영화 검색 메서드
def SearchMovie():
    print('▶ 영화 목록을 출력합니다.')
    
    for mKey, mInfo in movies.items():
        print('영화: {0}, 개봉연도: {1}, 국가: {2}'.format(mInfo[0], mInfo[1], mInfo[2]))
        
    return


# (추가 기능 5) 전체 감독 검색 메서드
def SearchDirector():
    print('▶ 감독 목록을 출력합니다.')
    
    for dKey, dInfo in directors.items():
        mov_key = dInfo[0]
        mov_title = GetMovieTitleByMovieKey(mov_key)
        
        print('감독이름: {0}, 연출작품: {1}'.format(dInfo[1], mov_title))
        
    return


# (추가 기능 6) 전체 배우 검색 메서드
def SearchActor():
    
    print('▶ 배우 목록을 출력합니다.')

    for aKey, aInfo in actors.items():
        mov_key = aInfo[0]
        mov_title = GetMovieTitleByMovieKey(mov_key)

        print('배우이름: {0}, 출연작품: {1}, 출생연도: {2}'.format(aInfo[1], mov_title, aInfo[2]))
        
    return