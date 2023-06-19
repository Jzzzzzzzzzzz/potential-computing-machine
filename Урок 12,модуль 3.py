import os
current_path=os.path.abspath(__file__)
print(current_path)
parent_path = os.path.join(current_path,'..')
print(parent_path)

'''def recurs(count):
    print(count)
    if count == 5:
        return
    recurs(count+1)

    print(count)

recurs(0)'''

def factorial(n):

    if n==1:
        return n
    else:
        return n*factorial(n-1)

print(factorial(3))


'''def get_all_files(path):
    for i_name in os.listdir(path):
        new_path =  os.path.join(current_path,i_name)
        if os.path.isdir(new_path):
            parent_path = os.path.join(current_path,i_name)
            print("Папка",i_name)
            get_all_files(new_path)
        else:
            print("-",i_name)

get_all_files(parent_path)
'''
#До встречи,удачи!!!
