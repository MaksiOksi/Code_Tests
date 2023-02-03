def get_city_info(city, country, population=''):
    if population:
        full_name = f'{city},{country},{population}'
    else:
        full_name = f'{city},{country}'
    return full_name.title()
