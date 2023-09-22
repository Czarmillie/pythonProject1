file_obj = open('account.txt', mode='r')
print(file_obj.readlines())
file_obj.seek(0)
print(file_obj.readlines())
file_obj.close()

