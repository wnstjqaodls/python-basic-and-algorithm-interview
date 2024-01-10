import cgi

form = cgi.FieldStorage()  # 사용자가 전송한 자료를 py에서 받기
irum = form['name'].value  # java : request.getparameter("name")
tel = form['phone'].value
gender = form['gen'].value
if gender == '남' : 
    gender = 'M'
else:
    gender = 'F'


print('content-type:text/html;charset=utf-8\n')
print('')
print("""
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
이름은 {0} , 전화는 {1} , 성별은 {2}
<a href='../index.html'>메인으로</a>
</body>
</html>
""".format(irum,tel,gender))