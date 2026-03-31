def count_names(prenoms):
    count = 0

    for prenom in prenoms:
        if len(prenom) > 7:
            count += 1

    return count

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]

print("Total :", count_names(prenoms))