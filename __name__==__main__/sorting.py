

def bubblesort(items : list[int]) -> list[int]:
    
    for i in range(len(items)):
        swapped = False

        for j in range(len(items) - i - 1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        
        if not swapped:
            break
    
    return items


print("testing my sort")

test_unsorted  =  [14, 1231, 2, 12, 5, 123, 24, 1]
print(f'unsorted: {test_unsorted}')


test_sorted = bubblesort(test_unsorted)
print(f'sorted: {test_sorted}')








def main():
    print("testing my sort")

    test_unsorted  =  [14, 1231, 2, 12, 5, 123, 24, 1]
    print(f'unsorted: {test_unsorted}')


    test_sorted = bubblesort(test_unsorted)
    print(f'sorted: {test_sorted}')


if __name__ == "__main__":
    #main()
    pass