import math as __math__

for name in dir(__math__):
    o=eval('__math__.'+name)
    if '__call__' in dir(o):
        exec('%s=__math__.%s'%(name.upper(), name))
    
def SUM(*args):
    print args
    ac=0
    for arg in args:
        ac+=arg
    return ac

def IF(*args):
    cond, t, f=args
    print cond, t, f
