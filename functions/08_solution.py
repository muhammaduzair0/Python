def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Python")
print_kwargs(name="Python", power="interpreter")
print_kwargs(name="Python", power="interpreter", abc="xyz")