def getCost():
	root=min(g_from)
	list1=[]
	list1.append(root)
	for i in range(g_nodes):
		for j in range(g_nodes):
			if(g_from[j]==root):
				temp=0
				temp=g_to[j]
				list1[i].append(temp)
			
		
	