# Mengurutkan bilagan

def susun_bilangan():
    bilangan = [22, 55, 10, 33, 66, 18, 19, 40, 76]
    return bilangan

# Ascending(Terkecil ke terbesar)
bilangan = susun_bilangan()
bilangan_terurut = sorted(bilangan)
print("Bilangan setelah disusun secara ascending:", bilangan_terurut)

# Descending (Terbesar ke terkecil)
bilangan_terurut = sorted(bilangan, reverse=True)
print("Bilangan setelah disusun secara descending:", bilangan_terurut)