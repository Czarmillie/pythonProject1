print(f"{'number':>6}{'square':>7}{'cube':>5}")

for number in range(6):
    square = number ** 2
    cube = number ** 3
    print(f"{number:>6}{square:>7}{cube:>5}")