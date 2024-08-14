x = '0.0'

try:
    float(x)
    print("X IS NUMBER")
except ValueError:
    if isinstance(x, str):
        print("X IS STRING")
    else:
        print("X IS A COMPLEX DATA TYPE")