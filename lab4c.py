#!/usr/bin/env python3

# Example dictionaries
dict_york = {'Address': '100 New Street', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

# Example lists for keys and values
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['100 New Street', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Combine the keys and values into a dictionary and return it
    return dict(zip(keys, values))

def shared_values(dict1, dict2):
    # Find shared values between two dictionaries
    return set(dict1.values()).intersection(dict2.values())

if __name__ == '__main__':
    # Create a dictionary from lists of keys and values
    york_dict = create_dictionary(list_keys, list_values)
    print('York Dictionary: ', york_dict)
    
    # Find and print the shared values between the two dictionaries
    common_values = shared_values(dict_york, dict_newnham)
    print('Shared Values:', common_values)

