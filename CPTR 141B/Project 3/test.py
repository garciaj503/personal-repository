address = "204 South College Ave, College Place, Wa 99324"
lines = address.split(",")
print(lines[0].replace("South","S"))
print(lines[1].strip())
print(lines[2].upper())