product_ids = [101, 102, 103, 104, 105]

pid = int(input("Enter Product ID: "))

for i in range(len(product_ids)):
    if product_ids[i] == pid:
        print("Product Found")
        break
else:
    print("Product Not Found")