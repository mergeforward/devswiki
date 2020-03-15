
def quick_sort(a):  
    if not a: return []  
    return quick_sort([x for x in a[1:] if x< a[0]]) + a[0:1] +  \
           quick_sort([x for x in a[1:] if x>=a[0]])  


if __name__ == "__main__":
    data = [10,16,8,12,15,6,3,9,5]
    result = quick_sort(data)
    print('before sort: ', data)
    print('after sort: ', result)
