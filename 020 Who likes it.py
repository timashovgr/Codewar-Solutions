#You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

def likes(names):
    if names == []:
        return 'no one likes this'
    if len(names) == 1:
        return names[0] + ' likes this'
    if len(names) == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    if len(names) == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    return names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + ' others like this'