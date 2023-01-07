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

def translate(z, object):
    '''
    translate
    ---
    core.translate
    '''
    while z < len(object):

        i = 0
        q = 0

        while q < len(object[z]):
            while i < 11:
                try:
                    place = [n for n in range(len(object[z])) if object[z][n:n + 2] == f'{i}(']
                    object[z] = f"{object[z][:place[q]]}*{object[z][place[q]:]}"

                    place = [n for n in range(len(object[z])) if object[z][n:n + 2] == f'){i}']
                    object[z] = f"{object[z][:place[q]]}*{object[z][place[q]:]}"

                except IndexError:
                    pass

                i += 1
            q += 1

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

    translate(z, object)
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
