
def multiple(num, max):
    multiples = []
    for x in xrange(max):
        if(x % num == 0):
            multiples.append(x)
    return multiples

def sum_of_multiples(max, a_list):
    multiples = []
    for num in a_list:
        multiples += multiple(num, max)

    multiples = list(set(multiples))
    return sum(multiples)
