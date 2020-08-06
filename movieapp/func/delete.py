from func.datapack import movies, directors, actors

# (추가 기능 1) 배우 데이터 삭제해보기
def DelActor():
    delAct_name = input('삭제할 배우 이름를 입력해주세요: ')
    
    isFound = False
    delAct_key = ''
    
    for aKey, aInfo in actors.items():
        
        if delAct_name == aInfo[1]:
            delAct_key = aKey
            
            isFound = True

    if isFound == True:
        actors.pop(delAct_key)
        
        print('▶ 해당 배우(\'{0}\')를 삭제하였습니다.'.format(delAct_name))
    
    else:
        print('▶ 해당 배우(\'{0}\')를 찾을 수 없습니다.'.format(delAct_name))
    
    return


# (추가 기능 2) 감독 데이터 삭제해보기
def DelDirector():
    delDir_name = input('삭제할 감독 이름를 입력해주세요: ')
    
    isFound = False
    delDir_key = ''
    
    for dKey, dInfo in directors.items():
        
        if delDir_name == dInfo[1]:
            delDir_key = dKey
            
            isFound = True

    if isFound == True:
        directors.pop(delDir_key)
        
        print('▶ 해당 감독(\'{0}\')을 삭제하였습니다.'.format(delDir_name))
    
    else:
        print('▶ 해당 감독(\'{0}\')을 찾을 수 없습니다.'.format(delDir_name))

    
    return


# (추가 기능 3) 영화 데이터 삭제해보기
def DelMovie():
    
    return