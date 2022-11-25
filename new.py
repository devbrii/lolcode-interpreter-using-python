list1 = "KD DK KDDD BTW NDSKJ DSKDJ DJSKS"

splitted_list = list1.split()
index = splitted_list.index("BTW")
print(index)

splitted_list = splitted_list[0:index]
print(splitted_list)