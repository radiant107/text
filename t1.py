data = []
progress = 0
with open('reviews.txt', 'r') as s:
	for s1 in s:
		data.append(s1.strip()) # 把每一筆留言去除/N後原封不動裝入清單
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
	if len(d1) < 100: # 篩選留言長度小於100
		new.append(d1)
print('總共有', len(new), '筆資料長度小於100')
print(new[0])

goodnew = []
for d1 in data:
	if 'good' in d1: # 篩選留言裡面有good的
		if 'great' in d1: # 再加篩選同時也有great的
			goodnew.append(d1)
print(len(goodnew))
print(goodnew[0])
print(goodnew[1])

# 清單快寫法, 把上面的簡化
good = [d for d in data if 'good' in d]
print('簡化法的', good[0])
print(len(good))

# 清單裡面也可以不要原封不動裝入，可以改裝其他東西
good1 = []
for d in data:
	if 'good' in d:
		good1.append('True') # 這邊寫入的True是string不是Boolean
print(good1[0])
print(len(good1))

# 簡化寫法 List comprehension
good1 = ['True' + '123' for d in data if 'good' in d]
print(good1[0])
print(len(good1))

# True and False篩選
bad1 = ['bad' in d for d in data] # 有bad的會被寫入True，沒有bad的就會被寫入False，這邊寫入的是Boolean
count1 = 0
count2 = 0
for b1 in bad1:
	if b1 == True:
		count1 += 1
	else:
		count2 += 1
print('總共有', count1, '筆留言提到bad')
print('總共有', count2, '筆留言沒有提到bad')
