"""Add item 7000 after 6000 in the following Python List"""

listing = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
listing[2][2].insert(2, 7000)
print(listing)

#or
listing = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
listing[2][2].append(7000)
print(listing)
