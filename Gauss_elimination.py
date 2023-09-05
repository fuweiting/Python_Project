from numpy import array, zeros, fabs, linalg

a = array([[7, 2, 3, 4],
           [2, 3, 3, 4],
           [7, 6, 9, 4],
           [8, 7, 6 ,5]], float)
b = array([2, 5, 8, 7], float)

n = len(b)
x = zeros(n, float)

# first loop specifys the fixed row
for k in range(n - 1):
    if fabs(a[k, k]) < 1.0e-12:

        for i in range(k + 1, n):
            if fabs(a[i, k]) > fabs(a[k, k]):
                a[[k, i]] = a[[i, k]]
                b[[k, i]] = b[[i, k]]           # row i and row k exchange
                break

    for j in range(k+1, n):
        factor = a[j, k]/a[k, k]
        a[[j]] = a[[j]] - factor*a[[k]]
        b[[j]] = b[[j]] - factor*b[[k]]

x[[n-1]] = b[[n-1]] = b[[n-1]]/a[n-1,n-1]
a[[n-1]] = a[[n-1]]/a[n-1,n-1]


for i in range(n-1):
    x[(n - 2) - i] = b[(n - 2) - i]
    for j in range(i+1):
        x[(n-2) - i] = x[(n-2) - i] - a[(n-2) - i, (n-1) - j] * x[(n-1) - j]
    x[(n - 2) - i] = x[(n - 2) - i] / a[(n - 2) - i, (n - 2) - i]



print(x)
print(linalg.solve(a, b))
