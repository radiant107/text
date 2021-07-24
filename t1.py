data = []
progress = 0
with open('reviews.txt', 'r') as s:
	for s1 in s:
		data.append(s1.strip())
		progress += 1
		if progress % 10000 == 0:
			print(len(data))

print(data[0])
sum_len = 0
for d1 in data:
	sum_len =  sum_len + len(d1)
print('留言平均長度為', sum_len / len(data), '字')

new =[]
for d1 in data:
	if len(d1) < 100:
		new.append(d1)
print('總共有', len(new), '筆資料長度小於100')
print(new[0])