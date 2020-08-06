# datapack에 있는 자료들과 연결하기
# from (  파일  ) import (  변수, 메서드  ): 다른 파일 내의 변수, 메서드 불러오기
from func.datapack import movies, directors, actors, command_message
from func.create import CreateKey         #그럼 얘도 없어도 되는 것 아냐? --> ㅇㅇ 맞아. 필요한 곳에서만 import 해주면 됨
from func.add import AddMovie, AddDirector, AddActor
from func.delete import DelMovie, DelDirector, DelActor
from func.search import SearchMovie, SearchDirector, SearchActor


# (실행) While을 활용해서 커맨드 이용한 반복 작업 만들기
def RunCommand(command):
    
    if command == '1':
        AddMovie()

    elif command == '2':
        AddDirector()

    elif command == '3':
        AddActor()

    elif command == '11':
        DelMovie()

    elif command == '12':
        DelDirector()

    elif command == '13':
        DelActor()

    elif command == '21':
        SearchMovie()

    elif command == '22':
        SearchDirector()

    elif command == '23':
        SearchActor()    
    
    return

command = ''

while command.upper() != 'EXIT':
    command = input(command_message)
    print('')
    
    try:
        RunCommand(command)
    except Exception as e:
        print('---------------<오류>---------------')
        print(e)
        print('------------------------------------')
    