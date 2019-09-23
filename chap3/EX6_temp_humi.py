temp = int(input("Enter today's temperature"))
humi = int(input("Enter today's Humiditiy"))
if temp >= 85 and humi > 60:
    print('Muggy day today')
elif temp >= 85:
        print('warm, but not muggy today')
elif temp >= 65:
        print('pleasent today')
elif temp <= 45:
        print('cold today')
else:
    print('cool today')      