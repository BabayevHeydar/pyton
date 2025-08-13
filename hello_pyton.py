# 1. İstifadəçidən iki ədəd al, hansının böyük olduğunu ekrana yazdır
a = float(input("Birinci ədədi daxil et: "))
b = float(input("İkinci ədədi daxil et: "))

if a > b:
    print("Birinci ədəd böyükdür:", a)
elif b > a:
    print("İkinci ədəd böyükdür:", b)
else:
    print("Hər ikisi bərabərdir.")

# 2. İstifadəçidən üç ədəd al və onların ortalamasını tap
x = float(input("1-ci ədəd: "))
y = float(input("2-ci ədəd: "))
z = float(input("3-cü ədəd: "))

ortalama = (x + y + z) / 3
print("Ortalama:", ortalama)

# 3. İstifadəçidən bir ədəd al, 0-dan kiçikdirsə → Mənfi, 0-a bərabərdirsə → Sıfır, əks halda → Müsbət
n = float(input("Bir ədəd daxil et: "))

if n < 0:
    print("Mənfi")
elif n == 0:
    print("Sıfır")
else:
    print("Müsbət")

# 4. İstifadəçidən ay nömrəsi al (1-12)
ay = int(input("Ay nömrəsini daxil et (1-12): "))

if ay in (1, 2, 12):
    print("Qış")
elif ay in (3, 4, 5):
    print("Yaz")
elif ay in (6, 7, 8):
    print("Yay")
else:
    print("Payız")

# 5. Yaş və sürücülük vəsiqəsi yoxlanışı
yas = int(input("Yaşını daxil et: "))

if yas >= 18:
    vesige = input("Sürücülük vəsiqən varmı? (bəli/xeyr): ").lower()
    if vesige == "bəli":
        print("Maşın sürə bilərsən")
    else:
        print("Vəsiqə lazım")
else:
    print("Yaş çatmır")