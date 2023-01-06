def addition(cond):
    '''
    addition
    -
    core.calculate.addition
    '''
    #eval(cond)
    cond = cond.replace(" ", "")
    cond = [int(x) for x in cond.split('+')]
    return sum(cond)


def read(target):
    return open(target).read().split('\n')

out = []
def output(result):
    out.append(result)


def compile(target):
    '''
    compile
    -
    core.compile
    '''

    object = read(target)


    z = 0

    while z < len(object):
        
        if 'sin' in object:
            pass

        if ' calculate ' in ' '+object[z]+' ':
            output(eval(f'{object[z - 1]}'))

        z += 1
        
    if z == len(object):
        z = 0

    while z < len(out):
        print(out[z])
        z += 1


compile("test.math")
