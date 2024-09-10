angka = list(map(int, input().split()))
a = int(input())
b = int(input())
for _ in range(b):
    temp = angka[:7-a]
    angka[:7-a] = angka[-a:]
    angka[-a:] = temp
d, e, f = map(int,input().split())
print(angka[d], angka[e], angka[f])
