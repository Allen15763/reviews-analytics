data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		# print(len(data)) 該條在for裡面，會重複印筆數直到100K完
		count += 1
		if count % 1000 == 0:  # 求餘數 % 1000
			print(len(data))
		
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for avg in data:
	sum_len += len(avg)

print('每筆留言平均長度為', round(sum_len/len(data),0), '字')
