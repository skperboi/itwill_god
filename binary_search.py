def binary_search(data, target) :
    first = 0
    mid = int(len(data)/2)
    last = len(data)
    ### 데이터 확인용 로그
    print('first:{}   mid:{}   last:{}'.format(first,mid,last))
    rr=[]
    for i in range(first,last-1) :
        rr.append(data[i])
    print(rr)
    ### 데이터 확인용 로그
    if (first==mid) or (last==mid) :
       if target==data[first] or target==data[last] :
           print('{} 이(은) 있습니다.'.format(target))
       else :
           print('{} 이(은) 없습니다.'.format(target))
       return 0
    elif target == data[mid] :
        print('{} 이(은) 있습니다.'.format(target))
        return 0
    elif target > data[mid] :
        data = data[mid:last]
    elif target < data[mid] :
        data = data[first:mid]  
        
    return binary_search(data, target)
    
data = [1,7,11,12,14,23,33,47,51,64,67,77,130,672,871]    

binary_search(data,13)