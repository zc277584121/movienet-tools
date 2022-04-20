def print_line():
    print('-' * 100)


def intersection(list1, list2):
    """
    Returns the intersection of two lists. 交集
    """
    return list(set(list1) & set(list2))


def difference(list1, list2):
    """
    Returns the difference of two lists. 差集（list1有, list2没有的）
    """
    return list(set(list1) - set(list2))


def union(list1, list2):
    """
    Returns the union of two lists. 并集
    """
    return list(set(list1) | set(list2))


