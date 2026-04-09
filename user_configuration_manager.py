test_settings = {
    'theme': 'light',
    'notifications': 'enabled',
    'language': 'english'
}

def add_setting(dict_of_settings, key_value_tuple):
    key, value = key_value_tuple
    key = key.lower()
    value = value.lower()
    
    if key in dict_of_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dict_of_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dict_of_settings, key_value_tuple):
    key, value = key_value_tuple
    
    key = key.lower()
    value = value.lower()

    if key in dict_of_settings:
        dict_of_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else: 
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dict_of_settings, key):
    key = key.lower()

    if key in dict_of_settings:
        del dict_of_settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(dict_of_settings):
    if not dict_of_settings:
        return "No settings available."
    
    settings_str = "Current User Settings:\n"
    
    for key, value in dict_of_settings.items():
        settings_str += f"{key.capitalize()}: {value}\n"
    
    return settings_str
