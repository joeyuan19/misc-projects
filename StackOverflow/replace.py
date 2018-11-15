def replace_item(obj, key, replace_value):
    """
    Replaces the dictionary value of key with replace_value in the obj dictionary.
    """
    if key in obj:
        obj[key] = replace_value
    for k, v in obj.items():
        if isinstance(v, dict):
            obj[k] = replace_item(v, key, replace_value)
    return obj

def replace_item(obj, key, replace_value):
    """
    Replaces the dictionary value of key with replace_value in the obj dictionary.
    """
    if key in obj:
        obj[key] = replace_value

    for k, v in obj.items():
        if isinstance(v, dict):
            replace_item(v, key, replace_value)

person_dict = {
    "name": "Alex",
    "sex": "M",
    "title": "Engineer",
    "work_type": "derp",
    "misc": {
        "mailbox": "3A",
        "work_type": "remote"
    }
}
replace_item(person_dict, "work_type", "office")
print(person_dict)
