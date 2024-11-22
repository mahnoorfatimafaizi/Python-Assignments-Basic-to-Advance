# Milestone #1: Mars Weight

MARS_CONSTANT: float = 0.378

def get_mars_weight():
    user_weight: float = float(input("Enter Your Earth's Weight: "))
    print(user_weight)


    mars_weight = round((user_weight * MARS_CONSTANT), 2)
    print(mars_weight)

    return f"Your Weight on Mars: {mars_weight}"

my_weight_on_mars = get_mars_weight()
print(my_weight_on_mars)