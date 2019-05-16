def rainfall_generator():
    rainfall_list = []
    for i in range(12):
        monthly_rain = float(input("Enter rain for month {}: ".format(i+1)))
        rainfall_list.append(monthly_rain)
    return rainfall_list

def rainfall_total(a):
    total = 0
    for monthly_rain in a:
        total += monthly_rain
    return total

def main():
    rainfall = rainfall_generator()
    total_rainfall = rainfall_total(rainfall)
    avg_monthly_rain = total_rainfall/12
    lowest_rain_month = rainfall.index(min(rainfall))
    highest_rain_month = rainfall.index(max(rainfall))
    print("Total Rainfall for the Year:",total_rainfall)
    print("Average monthly rain:",avg_monthly_rain)
    print("The month with the lowest rain is:",lowest_rain_month+1)
    print("The month with the highest rain is:",highest_rain_month+1)
main()