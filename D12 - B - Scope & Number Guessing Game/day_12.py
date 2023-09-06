# Modifying Global Scope
enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"Variable inside the function: {enemies}")


# Return Global Variable without changing its value
def return_global_variable():
    global enemies
    return enemies + 1


increase_enemies()
print(f"Variable outside the function: {enemies}")
print(f"Variable returned from the function: {return_global_variable()}")

# PYTHON CONSTANTS AND GLOBAL SCOPE
PI = 3.14159


