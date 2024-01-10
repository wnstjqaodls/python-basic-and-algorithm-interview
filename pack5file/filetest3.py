# 키보드로 동이름을 입력해 해당 자료읽기! 
try:
    dong = input('동이름 입력:')

    with open('zipcode.txt', mode='r', encoding='euc-kr') as f:
        line = f.readline()
        #print(line)
        
        while line:
            lines = line.split('\t')
            #print(lines)
            #break
            
            if lines[3].startswith('dong'): # 이 글자로 시작되는걸 찾아주는 함수
                #print(lines)
                print('[' +lines[0] + ']' + ' ' + lines[1] + \
                      ' ' + lines[2] + ' ' + lines[3] + ' ' + lines[4])
            
            line = f.readline()
            
     
except Exception as e:
    print('err',e)