def train_fare(age): 
    if age >= 12: 
       return 10000 
    elif age >= 6: 
       return 5000 
    else: 
       return 0
    
print(train_fare(12)) # => 10000 
print(train_fare(6)) # => 5000 
print(train_fare(5)) # => 0
