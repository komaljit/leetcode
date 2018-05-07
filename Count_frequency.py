"""
    method 1- brute force implementation
    time-complexity- n*m
"""


def get_count_bruteforce(st, sub_st):
    freq = 0
    if not sub_st:
        return freq
    for i in range(len(st)):
        if st[i] == sub_st[0]:
            start = 0
            while start < len(sub_st) and start+i < len(st):
                if st[i+start] != sub_st[start]:
                    break
                else:
                    start += 1
            if start == len(sub_st):
                freq += 1
    return freq


"""
    method 2- Rabin-Karp algorithm
    time-complexity- n
"""


def get_count_rabinkarp(st, sub_st):
    if len(st) < len(sub_st) or not sub_st:
        return 0
    st, sub_st = st.upper(),sub_st.upper()
    sub_st_hash = get_hash(sub_st)
    prev_hash = get_hash(st[:len(sub_st)])
    count = 1 if sub_st_hash == prev_hash else 0
    for i in range(len(sub_st),len(st)):
        cur_hash = new_hash(prev_hash, st[i], st[i-len(sub_st)], len(sub_st))
        if cur_hash == sub_st_hash:
            return i
        prev_hash = cur_hash
    return -1


# get initial hash
def get_hash(st):
    hash = 0
    for i in range(len(st)):
        hash += (ord(st[i]) - ord('A') + 1)* (3**(i+1))
    return hash


# get hash of current window
def new_hash(prev_hash,ch_add,ch_remove, l):
    return int(prev_hash/3) + (ord(ch_add)-ord('A')+1)* (3**l) - (ord(ch_remove)-ord('A') + 1)


# #  uncomment this section to run tets cases for get_count_bruteforce
# print(get_count_bruteforce("ab",""))
# print(get_count_bruteforce("a","a"))
# print(get_count_bruteforce("aaa","a"))
# print(get_count_bruteforce("cd","b"))


#  uncomment this section to run tets cases for rabin-karp algorithm
print(get_count_rabinkarp("abcdxyz","xyzabcd"))
# print(get_count_rabinkarp("a","a"))
# print(get_count_rabinkarp("aaa","a"))
# print(get_count_rabinkarp("cd","b"))
