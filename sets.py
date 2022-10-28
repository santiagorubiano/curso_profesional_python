

# def remove_dupliacates(some_list):
#     whithout_duplicates=[]
#     for element in some_list:
#         if element not in whithout_duplicates:
#             whithout_duplicates.append(element)
#     return whithout_duplicates

# def run():
#     random_list=[1,1,2,2,3,3,4,4]
#     print(remove_dupliacates(random_list))

# if __name__ == "__main__":
#     run()
    
def remove_dupliacates(some_list):
    return set(list(some_list))


def run():

    my_list=[1,2,3,4,5,6,1,2,3,7,8,9,1,10]
    print(remove_dupliacates(my_list))

if __name__ == "__main__":
    run()