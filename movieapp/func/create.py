# 고유번호 자동 생성 메서드
def CreateKey(pattern, dics):
    dic_count = len(dics) + 1
    dic_key = '{0}{1:0>3}'.format(pattern, dic_count)       #{0}에 들어가는 단어를 총 3글자로 하고, 나머지는 왼족으로 0을 추가한다는 뜻
    
    return dic_key