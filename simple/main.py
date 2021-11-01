from random import randint

def main():
    """ Function running de excersise"""
    ids_list = []
    for i in range(10):
        age = randint(1, 100)
        ids_list.append({'id': i, 'age':age})
    
    return ids_list

if __name__=='__main__':
    ids_list = main()
    print("printing ids_list:")
    print(ids_list)