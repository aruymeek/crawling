# 필요한 변수, 메서드 불러오기
from func.datapack import movies


# AddDirector와 AddActor에 필요한 도움을 주는 메서드
def FindMovieKey(title):         #영화 제목을 입력받아 영화 고유키 찾기
    isFound = False
    mov_key = ''
    
    for mKey, mInfo in movies.items():
        
        if title == mInfo[0]:
            mov_key = mKey
            
            isFound = True
            
    return isFound, mov_key


# Search 메서드에 도움을 주는 메서드
def GetMovieTitleByMovieKey(mov_key):       #영화 고유키로 영화 제목 반환하기
    
    mov = movies[mov_key]
    
    return mov[0]