# Faça um programa que receba os 3 lados de um triângulo e calcule sua área

s1 = float(input('lado 1 em cm: ').replace(',','.'))
s2 = float(input('lado 2 em cm: ').replace(',','.'))
s3 = float(input('lado 3 em cm: ').replace(',','.'))

# area = (s(s-s1)(s-s2)(s-s3))^(1/2)
# s = (s1+s2+s3)/2

s = (s1 + s2 + s3) / 2

area = (s * (s-s1) * (s-s2) * (s-s3)) ** 0.5

print(f'A área do triângulo é {area} ')