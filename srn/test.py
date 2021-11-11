import requests

a=-1
for i in range(0,10):
	base='01FB18EME00'
	a=a+1
	final=base+str(a)
	r=requests.post("https://pesuacademy.com/Academy/getStudentClassInfo", data={'loginId': final })
	print(r.text)

