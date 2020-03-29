# Problem:
# https://www.hackerrank.com/challenges/list-comprehensions/problem


# still need to work on this problem


squares_list = []

for i in range(1,11):
  squares_list.append(i*i)

print(squares_list)

#==================================

items_cost_list = [2.11, 4.10, 99.2, 54.90, .99 ]
tax_rate = .08

def add_tax_to_item(items_cost_list):
 return items_cost_list * (1+tax_rate)

total_after_tax = map(add_tax_to_item, items_cost_list)

print(list(total_after_tax))
