from colormappings import colors


colors.sort(key=lambda ci: ci[0])
hexvalues = [ci[1] for ci in colors]
hexnames = [ci[0] for ci in colors]
print(hexvalues)
print(hexnames)
