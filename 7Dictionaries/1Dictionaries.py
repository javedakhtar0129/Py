'''
We can make dictionary with {} braces,it is like comparator class in java.
There are keys & values.
1. Keys should be unique,cant be repeated.
2.
'''

customer = {
    "name":"JAVED AKHTAR",
    "Age": 30,
    "is_verified": True,
    34: 2131
}
print(customer)
print(customer["Age"])
print(customer[34])

# Above if we use a key that doesnt exist,then it gives error
# To overcome the error msg,we use get function
print(customer.get("is_verified"))
print(customer.get("asd"))  # This will only print None

# we can also modify dictionaries
customer["Birthday"] = "1 January"
print(customer.get("Birthday"))
