
temperature = 42.5
temperature_limit = 40.0

print("Robot temperature:", temperature, "C")

if temperature > temperature_limit:
    print("WARNING: High temperature")
else:
    print("Temperature is normal")
