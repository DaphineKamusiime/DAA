####solving a nested list
def flat(nested):
   # checking if list is empty
    if not(bool(nested)):
        return nested
 # checking if instance of list is empty or not
    if isinstance(nested[0], list):
 # calling function with sublist as argument
        return flat(*nested[:1]) + flat(nested[1:])
  # calling function with sublist as argument
    return nested[:1] + flat(nested[1:])
nested = ['a', ['b', ['c', ['d']], 'e'], 'f']
print('Nested List:', nested)
print("Flattened List:", flat(nested))