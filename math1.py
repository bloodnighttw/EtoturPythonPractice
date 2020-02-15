
#####################################################################
#																	#
#	Author:	Bloodnighttw											#
#	Github:	https://github.com/bloodnighttw/EtoturPythonPractice	#
#																	#
#####################################################################

while True:
	a , b , c = map(int , input().split())
	c = float ( (a+b)*c/2 )
	print("Trapezoid area:"+str(c))