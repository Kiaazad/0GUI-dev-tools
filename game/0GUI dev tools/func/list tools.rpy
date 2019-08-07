init -100 python:
    def find_in_nested_list(list, item):
        for sub_list in list:
            if item in sub_list:
                return (list.index(sub_list), sub_list.index(item))