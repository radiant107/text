with open('reviews.txt', 'r') as R: 
	data = [d for d in R]  # 讀入檔案字串的簡寫法

print(len(data))
print(data[0])

best1 = [a for a in data if 'best' in a]
print(len(best1))
print(best1[1])