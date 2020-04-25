data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		# print(len(data)) 該條在for裡面，會重複印筆數直到100K完
		count += 1
		if count % 1000 == 0:  # 求餘數 % 1000
			print(len(data))
		
print(len(data))


print(data[0])
print('-------------')
print(data[1])