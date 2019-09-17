def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if idx < 0:
        return my_list
    for x in copy:
        if x == idx:
            copy[x] = element
            return copy
        if x > idx:
            return my_list
