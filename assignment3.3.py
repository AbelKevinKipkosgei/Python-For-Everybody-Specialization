try:
    score = float(input("Enter a score between 0.0 and 1.0: "))
except:
    print(f"Error, please enter a numeric value!! ")
    quit()

if score > 1.0 or score < 0:
    print(f"Score is out of range!!")
elif score >= 0.9:
    print(f"A")
elif score >= 0.8:
    print(f"B")
elif score >= 0.7:
    print(f"C")
elif score >= 0.6:
    print(f"D")
elif score < 0.6:
    print(f"F")
