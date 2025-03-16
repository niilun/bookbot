# Key sorts
def sort_occurence(dict):
    return dict["count"]

# Convert a dict to a sorted list of dicts (by occurence)
def convert_to_sorted_list(dictionary):
    converted_list = []
    for key, value in dictionary.items():
        converted_list.append({"char": key, "count": value})
    
    converted_list.sort(reverse=True, key=sort_occurence)
    return converted_list