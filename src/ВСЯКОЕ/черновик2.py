n = int(input())
articul_sales = []

for _ in range(n):
    data = list(map(int, input().split()))
    articul = data[0]
    last_3_months_sales = sum(data[-3:])
    articul_sales.append((articul, last_3_months_sales))

best_selling_articul = max(articul_sales, key=lambda x: x[1])[0]

print(best_selling_articul)