arr = [2, 3, 65]

def Great(arr):
    try:
        if arr[0]**2 + arr[1]**2 == arr[2]**2:
            return True
        elif arr[0]**2 + arr[2]**2 == arr[1]**2:
            return True
        elif arr[1]**2 + arr[2]**2 == arr[0]**2:
            return True
        else:
            return False
    except IndexError:
        print("Error: There are not enough elements in the array to perform the operation.")
        return False
    except TypeError:
        print("Error: Numeric data type expected.")


result = Great(arr)
print(result)