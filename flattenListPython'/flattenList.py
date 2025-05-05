import functools
import operator

def main():
    l = [
    [1, 2, 3],
    [4, 5, 6],
    [7],
    [8, 9] ]   

    print(l)

    flat_list =  []

    # for loops
    #for row in l:
        #for col in row:
            #flat_list.append(col)

    # list comprehension
    #flat_list = [col for row in l for col in row]
    
    for sub in l:
        flat_list.extend(sub)


    print(flat_list)




if __name__ == "__main__":
    main()