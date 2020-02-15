
#####################################################################
#                                                                   #
#   NOTE:   There Have somethings Wrong in Anser 3                  #
#   Author: Bloodnighttw                                            #
#   Github: https://github.com/bloodnighttw/EtoturPythonPractice    #
#                                                                   #
#####################################################################


while True:
	a , b  = map(int , input().split())
	print(str(a) + "+" + str(b) + "=" +str(a+b))
	print(str(a) + "*" + str(b) + "=" +str(a*b))
	print(str(a) + "-" + str(b) + "=" +str(a-b))
	d = int(a/b)
	if a < 0 and b > 0:
		print(str(a) + "/" + str(b) + "=" +str(int(a/b-1))+"..."+str(a%b))
	elif a < 0 and b < 0:
		print(str(a) + "/" + str(b) + "=" +str(int((a/b) + 1))+"..."+str(int(a%b-b)))
	elif a>0 and b<0:
		print(str(a) + "/" + str(b) + "=" +str(int((a/b)))+"..."+str(int(a%b-b)))
	elif a>0 and b >0:
		print(str(a) + "/" + str(b) + "=" +str(int(a/b))+"..."+str(a%b))
