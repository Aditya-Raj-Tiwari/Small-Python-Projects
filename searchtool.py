def check():
    datafile = open('search.txt')
    found = False
    for line in datafile:
        if 'ucci' in line:
            found = True
            break

    return found


found = check()
if found:
    print('found')
else:
    print('not found')