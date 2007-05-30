
# CFG actions

from StupidSheet.backend.cellutils import *

# Generated rule actions

def arg_1_1():
  return lambda _yyy: (lambda x0: x0)(_yyy)

def arglist_12_1():
  return lambda _yyy: (lambda x0: [x0])(_yyy)

def calculated_4_15():
  return lambda _yyy: lambda z38: (lambda x0, x1: parse_cellref(['cellref','ABS',x1.symbolic_name]))(z38, _yyy)

def calculated_5_1():
  return lambda _yyy: (lambda x0: parse_cellref(['cellref',x0.symbolic_name]))(_yyy)

def expansion_10(x0):
  return (lambda x0: [ 'string', x0])(x0)

def expansion_11(x0):
  return lambda z47: lambda z16: lambda z15: lambda z14: (lambda x0, x1, x2: [x0]+x2)((lambda x0, x1, x2: [x0,x2])(z14, z15, z16), z47, x0)

def expansion_27(x0, x1, x2, x3):
  return lambda z30: (lambda x0, x1, x2: ['+',x0,x2])(z30, x0, x3(x2(x1)))

def expansion_28(x0, x1, x2, x3):
  return lambda z31: (lambda x0, x1, x2: ['-',x0,x2])(z31, x0, x3(x2(x1)))

def expansion_29(x0, x1, x2):
  return lambda z8: (lambda x0, x1, x2: ['/',x0,x2])(z8, x0, x2(x1))

def expansion_30(x0, x1, x2):
  return lambda z18: (lambda x0, x1, x2: ['*',x0,x2])(z18, x0, x2(x1))

def expansion_39(x0, x1):
  return lambda z33: (lambda x0, x1, x2: parse_cellref(['cellref',x0.symbolic_name,'ABS',str(int(x2))]))(z33, x0, x1)

def expansion_41(x0, x1, x2):
  return (x2(x1))(x0)

def expansion_44(x0, x1, x2, x3):
  return lambda z1: (lambda x0, x1, x2, x3: ['funcall',x0.symbolic_name,x2])(z1, x0, x2(x1), x3)

def expansion_45(x0, x1):
  return (lambda x0, x1: -x1)(x0, x1)

def expansion_46(x0):
  return (lambda x0: x0)(x0)

def expansion_47(x0):
  return (lambda x0: x0.val())(x0)

def expansion_48(x0, x1, x2, x3, x4):
  return (lambda x0, x1, x2: ['group',x1])(x0, x3(x2(x1)), x4)

def expansion_49(x0, x1, x2):
  return lambda z35: (lambda x0, x1, x2: [x0]+x2)(z35, x0, x2(x1))

def expansion_51(x0, x1):
  return lambda z5: lambda z4: (lambda x0, x1, x2, x3: parse_cellref(['cellref','ABS',x1.symbolic_name,'ABS',str(int(x3))]))(z4, z5, x0, x1)

def expansion_55(x0, x1, x2, x3, x4, x5):
  return ((x5(x4(x3(x2))))(x1))(x0)

def expansion_56(x0, x1):
  return lambda z12: (lambda x0: x0)((lambda x0, x1, x2: ['range',x0,x2])(z12, x0, x1))

def expansion_58(x0, x1, x2):
  return (lambda x0: x0)(x2(x1(x0)))

def expr_3():
  return lambda _yyy: (lambda x0: x0)(_yyy)

def list_11_17_27():
  return lambda _yyy: lambda z24: lambda z23: (lambda x0: [x0])((lambda x0, x1, x2: [x0,x2])(z23, z24, _yyy))

def list_11_17_27_38_1():
  return lambda _yyy: lambda z45: lambda z22: lambda z21: (lambda x0, x1: [x0])((lambda x0, x1, x2: [x0,x2])(z21, z22, z45), _yyy)

def new_calculated_action_2(first, continuation):
  return continuation(first)

def new_expansion_0(first, continuation):
  return continuation(first)

def new_list_11_17_27_1(first, continuation):
  return continuation(first)

def term_0():
  return lambda _yyy: (lambda x0: x0)(_yyy)


