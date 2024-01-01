def remove_redundant(list):
    ans=set()
    for i in list:
        if i is None:
            continue
        ans.add(i[14:-6])

    print("Data Processing Successful!!")
    return ans


# add roll number in place of '*', Initials of 1st and lastname in place of '#', name in place of '-'
# nr_list = {None,'face_database\\*****_##/------_------_3.png'}
# ars = remove_redundant(nr_list)
# print(ars)
