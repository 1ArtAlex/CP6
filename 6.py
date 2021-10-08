print("введите кол-во элементов массива")
try:
	n=int(input())
except ValueError:
	print("введены некорректные данные")
	exit()
if n>=0:
	if n>=2:
		array=[0]*n
		for x in range(n):
			try: 
				print ("введите элемент массива")
				array[x]=int(input())
			except ValueError:
					print("введены некорректные данные")
					exit()
		print ("массив равен:", array)
		try:
			print("введите DELTA")
			D=float(input())
		except ValueError:
			print("введены некорректные данные")
			exit()
		min=array[0]
		for x in range(1,n):
			if array[x]<min:
				min=array[x]
		m=0
		if D>0:
			for x in range(0,n):
				if array[x]-min==D:
					m+=1
			if m>=1:
				m=str(m)
				print("количество элементов, отличающихся от минимального на DELTA:"+k)
			else:
				print("нет элементов отличающихся от минимального на DELTA")
		elif D==0:
			for x in range(0,n):
				if array[x]==min:
					m+=1
			m-=1
			if m>=1:
				m=str(m)
				print("количество элементов, отличающихся от минимального на DELTA:"+k)
			else:
				print("нет элементов отличающихся от минимального на DELTA")
		else:
			print("введены некорректные данные")
	else:
		print ("введите минимум два элемента")
else:
	print("введены некорректные данные")
