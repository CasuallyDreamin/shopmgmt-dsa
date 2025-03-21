from hashtable import hashtable as ht

mht = ht()

mht.insert(20, 30)
mht.insert(20, 80)
mht.insert(30, 80)
mht.insert(50, 60)
mht.insert(1000, 413)
mht.insert("yasin", "arambash")

print(mht.get(1000))
