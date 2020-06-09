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

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100') #一英文字=一長度
print(new[0])
print(new[1])

#good = []
#for g in data:
#	if 'good' in g:
#		good.append(g)

# 補充if觀念 'a' in 'abc' -> True
# 補充if觀念 '1' in 'abc' -> False

good = [g for g in data if 'good' in g]  #27~30  list comprehension


print('一共有', len(good), '筆資料包含good')
print(good[0])
#print(good[1])

#bad = ['bad' in d for d in data]  #比對data所有含bad資料，回傳"所有"結果
#print(bad)

#46~48 = 42
#bad = []
#for d in data:
#	bad.append('bad' in d)

wc = {} #word_count
for d in data:
	words =d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1 #wc[word] 字典表示查找word這個字
		else:
			wc[word] = 1 #add into dic

for word in wc:
	if wc[word] > 100:
			print(word, wc[word])
print(len(wc))
print('your name:', wc['Allen'])

while True:
	word = input('請問你要查甚麼字: ')
	if word == 'q':
		break
	elif word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('There is no such word')
print('Thank you for Searching!')

