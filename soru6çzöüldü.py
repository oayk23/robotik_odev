def faktoriyel(a):
    if a == 1:
        return 1
    return faktoriyel(a-1)*a
print(faktoriyel(643))