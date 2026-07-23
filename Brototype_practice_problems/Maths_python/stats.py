# Mean function

def my_mean(data):
    total=0
    for x in data:
        total+=x
    avg=total/len(data)
    return avg

# Median function

def my_median(data):
    length=len(data)
    mid=length//2
    for i in range(length):
        for x in range(length-1): # [12, 15, 12, 18, 20, 12, 90]
            if data[x]>data[i]:
                temp=data[i]
                data[i]=data[x]
                data[x]=temp
    print(data)
    if length % 2 == 0:
        return (data[mid]+data[mid-1])/2
    else:
        return data[mid]
    
# Mode function

def my_mode(data):
    dict_freq={}
    for x in data:
        if x in dict_freq:
            dict_freq[x]=dict_freq[x]+1
        else:
            dict_freq[x]=1
    max_value=max(dict_freq.values())
    for key, value in dict_freq.items():
        if value==max_value:
            return key
        
# Variance function

def my_variance(data):
    avg=my_mean(data)
    summation=0
    for i in data:
        summation+=(i-avg)**2
    variance=summation/len(data)
    return variance

# Standard deviation
def my_std_dev(data):
    return my_variance(data)**0.5
        

    
