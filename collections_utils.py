import random


def RandomPickItemsFromArray(array, itemCount):
    if itemCount > len(array):
        return []
    return random.sample(array, itemCount)