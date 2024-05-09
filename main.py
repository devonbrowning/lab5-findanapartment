def apt_search1(city: str, max_rent: int, min_beds: int, pets_allowed: bool):
    if pets_allowed:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month... ')
    else:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments all within a budget of ${max_rent} per month... ')

apt_search1("Denver", 2000, 2, False)
apt_search1("Denver", 1800, 2, True)

# Function apt_search2 with optional parameters
def apt_search2(city: str, max_rent: int, min_beds: int = 2, pets_allowed: bool = False) -> str:
    if pets_allowed:
        return f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month...'
    else:
        return f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month...'

# Calling apt_search2 with arguments for min_beds and pets_allowed both omitted
result1 = apt_search2("Denver", 2000)
print(result1)

# Calling apt_search2 with just min_beds and no pets_allowed
result2 = apt_search2("New York", 1800, min_beds=1)
print(result2)

# Calling apt_search2 with just pets_allowed and not min_beds using named arguments
result3 = apt_search2("Los Angeles",2200, pets_allowed=True)
print(result3)

# Lambda Functions
plus_one_hundred = lambda x: x + 100
print(plus_one_hundred(50))


square_num = lambda x: x * x
print(square_num(8))


concatenate = lambda s: "-" + s
print(concatenate("Hello"))


divide_by_3 = lambda x: x / 3
print(divide_by_3(12))



