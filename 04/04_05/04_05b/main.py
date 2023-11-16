def has_unique_characters(data):
    return len(set(data)) == len(data)
    # set_data = set(data)
    # if len(set_data) == len(data):
    #     return True
    # return False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
