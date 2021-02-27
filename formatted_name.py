def get_formatted_name(first_name,last_name,middle_name=''):
    """返回完整的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name("John","jostar")
sports_star = get_formatted_name("Jojo","haerbin","nick")
print(musician)
print(sports_star)
