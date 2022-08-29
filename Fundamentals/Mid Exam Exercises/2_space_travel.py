command = input().split('||')
fuel = int(input())
ammo = int(input())
while True:
    for comm in command:
        current_command = comm.split()
        if current_command[0] == 'Titan':
            print(f"You have reached Titan, all passengers are safe.")
            exit()
        doing = current_command[0]
        value = int(current_command[1])
        if comm[0] == 'Titan':
            print(f"You have reached Titan, all passengers are safe.")
            break
        elif doing == 'Travel':
            fuel -= 1
            if fuel > 0:
                print(f"The spaceship travelled {value} light-years")
            else:
                print(f"Mission failed.")
                exit()
        elif doing == 'Enemy':
            if ammo >= value:
                ammo -= value
                print(f"An enemy with {value} armour is defeated.")
            elif ammo < value:
                if fuel > 2 * value:
                    fuel -= 2
                    print(f"An enemy with {value} armour is outmaneuvered.")
                else:
                    print(f"Mission failed.")
                    exit()
        elif doing == 'Repair':
            fuel += value
            ammo += value * 2
            print(f"Ammunitions added: {value * 2}.")
            print(f"Fuel added: {value}.")
if comm[0] == 'Titan':
    print(f"You have reached Titan, all passengers are safe.")
