from random import randint

def set_list():
    """ Function running de excersise"""
    ids_list = []
    for i in range(10):
        age = randint(1, 100)
        ids_list.append({'id': i, 'age':age})
    
    return ids_list

def sort_ids_list(ids_list: list):
    """This function sorts the list, prints oldest and youngest id, and returns the sorted list"""
    sorted_list = sorted(ids_list, key = lambda id: id['age'])
    
    youngest = sorted_list[0]['id']
    oldest = sorted_list[-1]['id']
    
    print(f'youngest person: id = {youngest}')
    print(f'oldest person: id = {oldest}')

    return sorted_list