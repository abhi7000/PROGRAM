def kangaroo(x1,v1,x2,v2):
	if(x1>x2 and v1>v2):
		#print("failed in 1")
		#print("error 1")
		return("NO")
	elif(x2>x1 and v2>v1):
		#print("failed in 2")
		return ("NO")
	else:
		if(x1<x2):
			try:
				rel_dis=int(x2-x1)
				rel_speed=int(v1-v2)
				true_false=rel_dis/rel_speed
			#print(true_false)
			except:
				return "NO"
			if(true_false%1==0):
				#print("failed in 3")
				#print(type(true_false)=='int')
				return ("YES")
			else:
				#print("failed in 4")
				return ("NO")
		else:
			#print("failed in 5")

			rel_dis=x1-x2
			rel_speed=v2-v1
			true_false=rel_dis/rel_speed
			if(type(true_false)=='int'):
				#print("failed in 6")

				return ("YES")
			else:
				#print("failed in 7")

				return ("NO")
result=kangaroo(43,2,70,2)
print(result)