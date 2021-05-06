# Solution 1
def process_numbers(num_list):
    temp = []

    # if input isnt a list
    if isinstance(num_list, list) == False:
        print('Not a list')
        return temp
    
    for item in num_list:
        if isinstance(item, int):
           temp.append(item)
        elif item.isnumeric() == True:
            temp.append(int(item))
    
    temp.sort()
    return temp


def process_names(name_list):
    temp = []
    
    # if input isnt a list
    if isinstance(name_list, list) == False:
        print('Not a list')
        return temp
    
    for item in name_list:
        if isinstance(item, str):
           if item.isnumeric() == True:
               continue
           temp.append(item)
    
    temp.sort()
    return temp

# Solution 2
"""
def process_numbers(unprocessed_list):
    
    processed_list = []
    if isinstance(unprocessed_list, list) == False:
        return processed_list
    
    for item in unprocessed_list:
        if isinstance(item, int):
            processed_list.append(item)
        elif isinstance(item, str):
            if item.isnumeric():
                converted_item = int(item)
                processed_list.append(converted_item)
    
    processed_list.sort()
    return processed_list


def process_names(unprocessed_list):
    
    processed_list = []

    if isinstance(unprocessed_list, list) == False:
        return processed_list
    
    for item in unprocessed_list:
        if isinstance(item, str):
            if item.isnumeric() == False:
                processed_list.append(item)
    
    processed_list.sort()
    return processed_list
"""