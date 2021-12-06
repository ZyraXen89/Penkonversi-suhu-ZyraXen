print("Alat konversi suhu (hanya dalam celcius)")
print("YANG COPAS CODINGAN TERUS NGAKU-NGAKU BIKIN SENDIRI, BESOK SHARELOC :v")
print("\n")

def menu():
    return
c = float(input("Masukkan suhu celcius: "))
    
choice = input(str("""
1. Reamur
2. Fahreinheit
3. Kelvin
Suhu yang ingin dikonversikan: """))


if choice == "1":
    r = (4/5 * c)
    print("Nilai jika dikonversikan ke Reamur adalah: ", r)
    
elif choice == "2":
    f = (9/5 * c + 32)
    print("Nilai jika dikonversikan ke Fahreinheit adalah: ", f)
    
elif choice == "3":
    k = (c + 273)
    print("Nilai jika dikonversikan ke Kelvin adalah: ", k)
print("\n")
print("Dah gitu doang, aku gak ngerti cara pake ""break"" :v")