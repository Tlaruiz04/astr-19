import numpy as np
import math

def sin_tables(start, end, n_entries):
    x_values = np.linspace(start, end, n_entries)
    sin_values = [math.sin(x) for x in x_values]
    table = list(zip(x_values, sin_values))
    return table
def main():
    sin_table = sin_tables(0, 6.28, 1000) #6.28 is 2pi
    for x, sin_x, in sin_table:
        print(f"x: {x:.3f}, sin(x): {sin_x:.3f}")
if __name__ == "__main__":
    main()
