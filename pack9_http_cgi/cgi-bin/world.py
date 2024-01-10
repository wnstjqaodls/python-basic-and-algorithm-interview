s1 = '자료1'
s2 = '두번째자료'
s3 = 123123



print('content-type:text/html;charset=utf-8\n')
print('')
print('')
print("""
<html>
<head>
<body>
<h2>월드 만세</h2>
자료출력 : {0},{1},{2}<br>
자료출력 : {2}
<hr>
<img src ='../images/google.png' width='60%' />
<br>
<br>
<a href='../index.html'>메인으로</a>
</body></html>
""".format(s1,s2,s3))



print('')