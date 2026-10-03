
isim = input("Adın nedir?")
dogum_yılı = input("Hangi yılda doğdun?")
ay = input("Hangi ayda doğdun?")
yaş = 2026 - int(dogum_yılı)
ay = int(ay)
if ay >= 10:
    yaş = yaş - 1
print(f"Merhaba {isim}, demek {yaş} yaşındasın")

if yaş < 18:
    print("Demek daha reşit değilsin")

elif yaş >= 18 and ay <= 10:
    print(f"Bu harika {isim} demek reşitsin")
elif yaş >= 18 and ay >= 10:
    yaş = yaş + 1
    print(f"Bu harika {isim} demek neredeyse reşitsin az daha sabret")
print("Elveada")