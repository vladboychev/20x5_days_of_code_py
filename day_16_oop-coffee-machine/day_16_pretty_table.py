from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Artist", ["Sting", "U2", "Cure", "Sade"])
table.add_column("Song", ["Fragile", "One", "Wish", "Paradise"])
table.align = "l"
table.sortby = "Artist"

print(table)
