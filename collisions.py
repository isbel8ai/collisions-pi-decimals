pi_decimals = 7

first_mass = 100 ** pi_decimals
second_mass = 1

first_speed = (first_mass - second_mass) / (first_mass + second_mass)
second_speed = -2 * first_mass / (first_mass + second_mass)

count = 2

while first_speed > second_speed:
    new_first_speed = (first_speed * (first_mass - second_mass) + 2 * second_speed * second_mass) / (
                first_mass + second_mass)
    new_second_speed = (second_speed * (second_mass - first_mass) + 2 * first_speed * first_mass) / (
                first_mass + second_mass)
    first_speed = new_first_speed
    second_speed = new_second_speed * -1
    count += 2

if second_speed >= 0:
    count -= 1

print(count)
print(count / 10 ** pi_decimals)
