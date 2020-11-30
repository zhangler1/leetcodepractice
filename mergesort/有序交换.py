leftpresum=[1,3,6,87,134]
rightpresum =[12,32,62,872,1342]
l=0
r=0
while (l < len(leftpresum) and r < len((rightpresum))):

    if leftpresum[l] > rightpresum[r]:
        leftpresum[l], rightpresum[r] = rightpresum[r], leftpresum[l]
        r += 1

    elif leftpresum[l] < rightpresum[r]:
        l += 1
    else:
        r += 1
        l += 1