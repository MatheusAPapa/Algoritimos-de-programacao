grausF = 30
grausC = 0
for grausF in range(30, 51, 2):
    grausC = (grausF - 32) * 5/9
    print(f'{grausF}°F = {grausC    }°C')
