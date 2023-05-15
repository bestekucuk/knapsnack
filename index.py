# Dosya adını ve çanta kapasitesini kullanıcıdan alın
filename = input("Dosya adını girin: ")


# Dosyayı aç ve ağırlık ve değerleri oku
with open(filename, 'r') as f:
       line = f.readline().strip().split()
       capacity = int(line[1])
       lines = f.readlines()[1:]
       values = []
       weights = []
       for line in lines:
         value, weight = map(int, line.strip().split())
         values.append(value)
         weights.append(weight)
       n= len(weights)

# 0-1 Sırt Çantası problemi için dinamik programlama kullanarak çözüm oluştur
def knapsack(capacity, weights, values, n):
    K = [[0 for x in range(capacity+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(capacity+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][capacity]

# Sonuçları yazdır
result = knapsack(capacity, weights, values, n)
print("Çanta kapasitesi:", capacity)
print("Ağırlıklar:", weights)
print("Değerler:", values)
print("En yüksek değer:", result)
