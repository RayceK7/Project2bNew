import random

def quick_sort(values):

    comparisons =  0
    def sort(items):

        nonlocal comparisons
        if len(items)  <=  1:
            return items
        pivot = random.choice(items)
        left = []
        middle = []
        right = []

        for item in  items:
            if item< pivot:
                comparisons  += 1
                left.append( item )

            elif item > pivot:
                comparisons += 2
                right. append(item)

            else:
                comparisons += 2
                middle.append(item)

        return sort(left) + middle + sort(right)

    return sort( values), comparisons
