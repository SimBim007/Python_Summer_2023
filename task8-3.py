def sor_t(word):
    return len(set(word))
lst=['abab','xx','aaaaaaa','abcbab']
print(sorted(lst, key=lambda x:(-sor_t(x),x)))