import sys
import time

# Başlangıç zamanını kaydet
baslangic_zamani = time.time()
# Dinamik programlama ile 1-0 Knapsack problemini çözen fonksiyon
def solve_knapsack(items, n, capacity):
    # Değerleri ağırlığa oranla sırala
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    # Seçilen elemanların ağırlığı ve toplam değeri tutacak değişkenleri tanımla
    selected_weight = 0
    max_value = 0
    # Seçilen elemanların ağırlığını tutacak bir liste oluştur
    selected_items = []

    # Elemanları sırayla al ve kapasiteye sığdığı sürece seç
    for i in range(n):
        if selected_weight + items[i][0] <= capacity:
            selected_items.append(items[i][0])
            selected_weight += items[i][0]
            max_value += items[i][1]
            print((i+1),end=" ")
    
    # Seçilen elemanların ağırlığını ve toplam değerini döndür
    return selected_items, max_value

# Dosya ismini ve dosya yolunu al
filename = input("Dosya adını girin: ")
filepath = f"{filename}"

# Dosyayı satır satır oku ve ihtiyacımız olan verileri al
with open(filepath, "r") as f:
    # İlk satırdan toplam eleman sayısı ve çanta kapasitesini al
    line = f.readline().strip().split()
    n, capacity = int(line[0]), int(line[1])

    # Her bir elemanın ağırlığını ve değerini oku ve tuple olarak items listesine ekle
    items = []
    for i in range(n):
        line = f.readline().strip().split()
        weight, value = int(line[1]), int(line[0])
        items.append((weight, value))

# Knapsack problemini çöz
selected_items, max_value = solve_knapsack(items, n, capacity)

# Sonuçları yazdır
print(f"Toplam değer: {max_value}")
print("Seçilen elemanların ağırlığı:")
print(*selected_items)
print(selected_items)
# Seçilen elemanların ağırlığını yazdır
print("Seçilen elemanların ağırlığı:")
for item in items:
    if item[0] in selected_items:
        print("1", end=" ")
    else:
        print("0", end=" ")

bitis_zamani = time.time()

# Geçen süreyi hesapla
gecen_sure = bitis_zamani - baslangic_zamani

print("Geçen süre:", gecen_sure, "saniye")