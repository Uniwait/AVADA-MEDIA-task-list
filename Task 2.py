zombies=[2, 1, 1, 1  ] 
plants=[ 3, 2, 1, 1 ]

def service (plants, zombies):

    plants_is_winning = 0
    zombies_is_winning = 0
    try:
        if len(plants) < len(zombies):
            return False
        elif len(plants) > len(zombies):
            return True
        
        for i in range(len(plants)):
            if plants[i] > zombies[i]:
                plants_is_winning += 1
            elif plants[i] < zombies[i]:
                zombies_is_winning += 1
            elif plants[i] == zombies[i]:
                continue
            
        if zombies_is_winning == plants_is_winning:
            if sum(plants) > sum(zombies):
                return True
            elif sum(plants) < sum(zombies):
                return False
            elif sum(plants) == sum(zombies):
                return True
        elif zombies_is_winning > plants_is_winning:
            return False
        else:
            return True   
    except TypeError:
        print("Error: Expected a numerical data type.")
        
result = service(plants, zombies)
print(result)