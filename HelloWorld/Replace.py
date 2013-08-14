__author__ = 'alihooke'


def replace(input, find, replaceWith):
    """
replaces all occurrences of find with replaceWith

    """
    for i in range(len(input)):
        if input[i] == find:
            input[i]=replaceWith