data = []
with open('reviews.txt','r') as f:#r是讀寫的意思,打開檔案並讀取取名為file
	for line in f:#for 去讀出in在file裡面的資料
		data.append(line.strip()) #strip可以去掉字串中的空格
print(len(data))
print(data[0])