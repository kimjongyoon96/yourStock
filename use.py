file_path = 'C:\\Users\\Administrator\\yourStock\\test.txt'
labels =open(file_path).read().splitlines()

client_id =labels[0] 
client_secret=labels[1]

print(client_id,client_secret)