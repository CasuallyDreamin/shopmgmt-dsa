from hashtable import hashtable as ht
with open('delivered_parcel.txt','r') as f:
    raw = f.read().split('\n')
    raw.pop()
    data = [line.split(',') for line in raw]