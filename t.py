data = []
count = 0
with open('reviews.txt', 'r') as a:
	for line in a:
		data.append(line.strip())
		count += 1
		if count % 100000 == 0: # count和100000去求餘數為0
			print(len(data))

print('檔案讀取完了，總共有', len(data),'筆資料')


print('-----------')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度是', sum_len/len(data))
