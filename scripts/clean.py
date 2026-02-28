
with open("../data/raw.txt.py", "r") as f:
    lines = f.readlines()


data = []
for line in lines:
    year, pop = line.strip().split(",")
    data.append({
        "year": int(year),
        "population": float(pop)
    })


print("讀取資料:", data)

# 計算平均人口
total_population = sum(item["population"] for item in data)
average_population = total_population / len(data)
print("平均人口:", average_population)


growth_rates = []
for i in range(1, len(data)):
    previous = data[i-1]["population"]
    current = data[i]["population"]
    rate = (current - previous) / previous * 100
    growth_rates.append({
        "from_year": data[i-1]["year"],
        "to_year": data[i]["year"],
        "growth_rate": round(rate, 2)
    })
print("人口成長率:", growth_rates)


first_pop = data[0]["population"]
last_pop = data[-1]["population"]
years = data[-1]["year"] - data[0]["year"]
cagr = (last_pop / first_pop) ** (1/years) - 1
cagr_percentage = round(cagr * 100, 2)
print("CAGR:", cagr_percentage, "%")