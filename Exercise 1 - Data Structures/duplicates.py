list = [0, 1, 1, 7, 2, 3, 4, 5, 6, 7, 0, 8, 9, 1, 3, 6, 9, 0]


def remove_duplicates(list):
    final_list = []
    for i in list:
        if i not in final_list:
            final_list.append(i)

    return final_list


list = remove_duplicates(list)
