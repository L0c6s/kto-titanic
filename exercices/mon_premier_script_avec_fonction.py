def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print(prenom + " > 7")
        else:
            print(prenom + " <= 7")
    return more_than_seven


prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]

print("Total :", names(prenoms))