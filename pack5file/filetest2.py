# with 쓰면 close 자동

try: 
    
    # 파일저장
    with open('ftest3',mode = 'w' , encoding='utf-8') as f1:
        f1.write('요즘 날씨가 계속 흐려\n')
        f1.write('몸이 찌푸둥해\n')
    print('저장완료')
    
    with open('ftest3' , 'r' , encoding = 'UTF-8') as f2:
        print(f2.read())
except Exception as e:
    print('err',e)
    
    
print('\n 피클링(객체를저장하고읽기) --')
import pickle

try:
    
    dicData = {'tom' : '111-1111', '준섭' : '222-2222'}
    listData = ['abc','cdd']
    tupleData = (dicData,listData)
    
    with open('hello.dat',mode ='wb') as f3:
        pickle.dump(tupleData,f3)
        pickle.dump(listData,f3)
    print('객체를 파일로 저장 완료')
    
    with open('hello.dat','rb') as f4:
        a,b = pickle.load(f4)  #피클로저장된 객체읽기
        print(a)
        print(b)
        c = pickle.load(f4)
        print(c)
    
    
except Exception as e:
    print('err2',e)