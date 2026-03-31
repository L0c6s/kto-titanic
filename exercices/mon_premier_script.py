message = "C'est mon premier script !!!"
print(message)

je_change_de_type = 1
print(type(je_change_de_type))

je_change_de_type = "coucou"
print(type(je_change_de_type))

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
more_than_seven = 0

for prenom in prenoms:
    if len(prenom) > 7:
        more_than_seven += 1
        print(prenom + " > 7")
    else:
        print(prenom + " <= 7")

print("Total :", more_than_seven)