data = []
with open('reviews.txt','r') as f:#r是讀寫的意思,打開檔案並讀取取名為file
	for line in f:#for 去讀出in在file裡面的資料
		data.append(line.strip()) #strip可以去掉字串中的空格
#print(len(data))


sum_len = 0
for d in data:
	sum_len += len(d)
print('每筆留言長度平均是',sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'筆資料長度小於100') 