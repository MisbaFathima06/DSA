list1=[8,4,3,4,9,10,25,0,1,6]
key=int(input("Enter the key: "))

def linear_search(list1):       #goes through each index of the list
    for i in range(len(list1)):
        if(list1[i]==key):      #If the element at that index matches the key, return the index.
            return i
    return -1

print(linear_search(list1))