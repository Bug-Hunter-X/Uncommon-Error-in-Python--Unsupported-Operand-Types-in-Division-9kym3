def function_with_uncommon_error(a, b):
    try:
        if isinstance(b, (int, float)):
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            result = a / b
            return result
        else:
            raise TypeError("Unsupported operand type(s) for /'")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
result1 = function_with_uncommon_error(10, 2) 
print(f"Result1: {result1}")

result2 = function_with_uncommon_error(10, "hello")
print(f"Result2: {result2}")

result3 = function_with_uncommon_error(10, 0)
print(f"Result3: {result3}")

result4 = function_with_uncommon_error(10, [1,2,3])
print(f"Result4: {result4}") 