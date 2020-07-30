# Solving Compare the Triplets problem from hackerrank
# Jadon Paulse
# 18/5/2020

a = list(map(int, (input().split())))
b = list(map(int, (input().split())))
aliceScore = sum([(1 if a[i] > b[i] else 0)for i in range(3)])
bobScore = sum([(1 if a[i] < b[i] else 0)for i in range(3)])

# for i in range(3):
#     if a[i]>b[i]:
#         aliceScore = aliceScore + 1
#     if a[i]<b[i]:
#         bobScore = bobScore + 1
print(aliceScore, bobScore)

