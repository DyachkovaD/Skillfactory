import time

def my_deco():
    def wrapper():
        start = time.time()
        n, m = 3, 5
        a = [2, 8, 8]
        b = [3, 4, 5, 5, 10]
        i = j = 0 # указатели
        sort = []
        while i < n and j < m:
            if a[i] < b[j]:
                sort.append(a[i])
                i += 1
            else:
                sort.append(b[j])
                j += 1
        
        if i == n:
            sort += b[j:]
        elif j == m:
            sort += a[i:]
        print(sort)
        
        exit = time.time() - start
        return exit
    return wrapper()
        
d = my_deco()
print(d)

import time

def my_deco():
    def wrapper():
        start = time.time()
        n, m = 3, 5
        a = [2, 8, 8]
        b = [3, 4, 5, 5, 10]
        i = j = 0 # указатели
        sort = []
        while i < n and j < m:
            if a[i] < b[j]:
                sort.append(a[i])
                i += 1
            else:
                sort.append(b[j])
                j += 1
        
        while i < n:
            sort.append(a[i])
            i += 1
        while j < m:
            sort.append(b[j])
            j += 1
        print(sort)
        
        exit = time.time() - start
        return exit
    return wrapper()
        
d = my_deco()
print(d)
# n, m = 3, 5
# a = [2, 8, 8]
# b = [3, 4, 5, 5, 10]
# i = j = 0 # указатели
# sort = []
# while i < n and j < m:
#     if a[i] < b[j]:
#         sort.append(a[i])
#         i += 1
#     else:
#         sort.append(b[j])
#         j += 1

# if i == n:
#     sort += b[j:]
# elif j == m:
#     sort += a[i:]
# print(sort)