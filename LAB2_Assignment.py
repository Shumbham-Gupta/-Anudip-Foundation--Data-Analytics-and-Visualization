

# import numpy as np

# #problem 1
# temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
# hot_days=temperatures[temperatures>35]
# print("hot days",hot_days)
# cold_days=temperatures[temperatures<5]
# print("colder days are",cold_days)


# #problem 2
# monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
# quarterly_sales=monthly_sales.reshape(4,3)
# print("Quarter data is :",quarterly_sales)


# #problem 3
# customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
# last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
# recent_purchase_mask = last_purchase_days_ago <= 30
# recent_customers = customer_ids[recent_purchase_mask]
# non_recent_customers = customer_ids[~recent_purchase_mask]
# print("Customers who made a purchase in the last 30 days:")
# print(recent_customers)
# print("Customers who haven't made a purchase in the last 30 days:")
# print(non_recent_customers)


# #problem4
# full_time_employees = np.array([
#  [101, 'John Doe', 'Full-Time', 55000],
#  [102, 'Jane Smith', 'Full-Time', 60000],
#  [103, 'Mike Johnson', 'Full-Time', 52000]
#  ])
# part_time_employees = np.array([
#  [201, 'Alice Brown', 'Part-Time', 25000],
#  [202, 'Bob Wilson', 'Part-Time', 28000],
#  [203, 'Emily Davis', 'Part-Time', 22000]
#  ])
# whole_data=np.concatenate(full_time_employees,part_time_employees)
# print(whole_data)


# #problem 5
# list_of_arrays = [
#     np.array([3, 2, 8, 9]),
#     np.array([4, 12, 34, 25, 78]),
#     np.array([23, 12, 67])
# ]
# means = [np.mean(array) for array in list_of_arrays]
# print("Means of each array in the list:")
# print(means)


# #problem6
# x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
# median_value = np.median(x_odd)
# print("Median of the array:")
# print(median_value)


# #problem 7
# arr = np.array([20, 2, 7, 1, 34])
# standardDeviation=np.std(arr)
# print("standard deviation is :",standardDeviation)


# #problem8 
# house_prices = np.loadtxt('house_prices.csv', delimiter=',')
# average_price = np.mean(house_prices)
# print("Average house price:", average_price)
# high_prices = house_prices[house_prices > average_price]
# print("House prices above the average:", high_prices)
# np.savetxt('high_prices.csv', high_prices, delimiter=',', fmt='%f')
# print("High prices have been saved to 'high_prices.csv'")