def breakingRecords(scores):
	min=scores[0]
	max=scores[0]
	min_record=[]
	max_record=[]
	for i in range(1,len(scores)):
		if(min>scores[i]):
			min=scores[i]
			min_record.append(i)
		if(max<scores[i]):
			max=scores[i]
			max_record.append(i)
	times=[]
	times.append(len(max_record))
	times.append(len(min_record))
	return (times)
scores=[10,5,20,20,4,5,2,25,1]
result=breakingRecords(scores)

			