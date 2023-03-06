A = [int(x) for x in input().split()]
print(A)
print(max(A))
A.reverse()
print(A)
avg = sum(A) / len(A)
print(avg)
print([avg if x == 0 else x for x in A])