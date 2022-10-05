daten = "vorname ; nachname ; alter ; gewicht ; länge"
einzeldaten = daten.split(" ; ")
nameNDates = daten.split(" ; ", 2) #split at the first 2 semicolons,
print(einzeldaten)
print(nameNDates)