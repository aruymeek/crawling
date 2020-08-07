############### 재귀함수 Recrusive ###############
### 재귀함수: 메서드 내에서 자기 자신을 포함하여 반복적으로 호출할 수 있도록 한다
def Test1(num_count):

    num_count -= 1
    print('num: {0}'.format(num_count))

    if num_count > 0:
        Test1(num_count)      #자기 자신이지만 또 Test1로 돌아가서 반복. num_count가 0보다 큰 값이면 다시 위부터 실행(반복)

# 메서드 호출 (실행)
Test1(10)


### 탐색기 기능 구현해보기
import os

def FindDir(dir_name, depth):

    #listdir(): 해당 경로 안에 있는 폴더, 파일명 전부 리스트로 가져오기
    dirs = os.listdir(dir_name)

    for dir in dirs:

        dirType = '[D]'
        pathName = os.path.join(dir_name, dir)
        #os.path.getsize(): 파일 크기 / format(###, ','): 1,000단위 구분기호 형식
        size = format(os.path.getsize(pathName), ',')   

        #isfile(): 파일인지 아닌지를 bool 값으로 반환
        if os.path.isfile(pathName):
            dirType = '[F]'

        #'     ' * depth: 공백을 depth만큼 곱해주겠다 (문자열 곱셈) --> 파일의 계층구조를 확인할 수 있도록
        print('{0}{1} {2}  {3} Byte'.format('     ' * depth, dirType, dir, size))       

        #isdir(): 폴더인지 아닌지 bool 값으로 반환
        if os.path.isdir(pathName):
            # ★다시 이해해보기★ 반복호출, pathName이 디렉토리(폴더)이면 FindDir 반복 실행, 파일이면 for문 반복       
            FindDir(pathName, depth + 1)

        #listdir이 폴더와 파일을 전부 가져오므로, 구분할 수 있도록 try~except를 사용해줄 수도 있음
        #try:
            #FindDir(os.path.join(dir_name, dir), depth + 1)   #하위 경로로 이동하면서 depth가 1씩 증가됨을 나타냄
        #except:    #파일이면 더 이상 하위 경로로 진행할 수 없으므로 FindDir이 더 실행되지 않고 오류가 표시됨
            #print('{0}(임시 오류)'.format('     ' * depth))

# 실행
FindDir('C:/Users/671/Desktop/y/python', 1)
#FindDir('C:/Program Files (x86)', 1)
   # '액세스가 거부되었습니다.' 라는 오류메시지가 뜨는 이유? : 접근하면 안되는 폴더일 경우에 뜬다

