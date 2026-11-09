"""Merge Sort"""

def merge_sort(values):

    comparisons =  0
    def sort(items):

        nonlocal comparisons
        if len(items)  <= 1:
             return items
        middle =  len(items)// 2
        left = sort(items[ :middle])
        right =  sort(items[middle:])
        merged =[]
        i =0
        j = 0

        while i < len(left) and j < len(right):

            comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1

            else:
                merged.append(right[j]); j += 1

        merged.extend(left[i:] )
        merged.extend(right[j:])
        return merged
    return sort(values),  comparisons
