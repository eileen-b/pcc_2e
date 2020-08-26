"""Positional Arguments, page132-134 """
def describe_pet(animal_type, pet_name):
    '''Display information about a pet.'''
    print(f"\nI have a {animal_type.lower()}.")
    print(f"My {animal_type.lower()}'s name is {pet_name.title()}.")

print('------------------------')
print('Without kwarg, positions are important')
print('------------------------')
describe_pet('Cat', 'Nocto')
describe_pet('rug','rabbit')
print('------------------------')
print('Use kwarg to reduce the guess work,')
print('------------------------')
describe_pet(animal_type='cat', pet_name='Nocto')
describe_pet(pet_name='Rug',animal_type='rabbit')


