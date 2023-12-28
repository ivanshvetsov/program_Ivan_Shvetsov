A = int(input("введите сторону A: " ))
B = int(input("введите сторону B: " ))
C = int(input("введите сторону C: " ))
ramen = 0
CvA = 0
Cvb = 0
while A>= C:
    A-= C
    CvA += 1

while B >= C:
    B -= C
    Cvb += 1
for i in range(Cvb):
    ramen += CvA
print(ramen)
