def max_integer(my_list=None):
    if my_list is None:
        return None
    sorted_list = sorted(my_list)
    return sorted_list[-1] if sorted_list else None
