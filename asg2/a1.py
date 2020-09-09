price = [9.95, 14.95, 19.95, 24.95, 29.95, 34.95, 39.95, 44.95, 49.95]
discount = range(5, 51, 5)
row_format = "{:>15}" * (len(price) + 1)
print(row_format.format("Normal price:", *price))
for d in discount:
	K = 1 - (float(d)/100)
	prices_adj = [(round((p*K), 2)) for p in price]
	print(row_format.format("{0} % ".format(d), *prices_adj))