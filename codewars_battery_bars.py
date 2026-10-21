def battery_bars(percent):

    bars = percent // 20
    print(bars, 5 - bars)

    res = "[" + '#' * bars + '.' * (5 - bars) + ']'

    return res

print(battery_bars(100), "[#####]")
print(battery_bars(70), "[###..]")
print(battery_bars(20), "[#....]")
print(battery_bars(19), "[.....]")