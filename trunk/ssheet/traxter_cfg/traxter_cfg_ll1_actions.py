
# CFG actions

from cellutils import *

# Generated rule actions

def arg_1_1():
  return lambda _yyy: (lambda x0: x0)(_yyy)

def arglist_11_1():
  return lambda _yyy: (lambda x0: [x0])(_yyy)

def calculated_4_15():
  return lambda _yyy: lambda z30: (lambda x0, x1: parse_cellref(['cellref','ABS',x1.symbolic_name]))(z30, _yyy)

def calculated_5_1():
  return lambda _yyy: (lambda x0: parse_cellref(['cellref',x0.symbolic_name]))(_yyy)

def expansion_13(x0):
  return lambda z14: lambda z13: lambda z12: lambda z3: (lambda x0, x1, x2: [x0]+x2)((lambda x0, x1, x2: (x0,x2))(z3, z12, z13), z14, x0)

def expansion_26(x0, x1, x2, x3):
  return lambda z10: (lambda x0, x1, x2: ['+',x0,x2])(z10, x0, x3(x2(x1)))

def expansion_27(x0, x1, x2, x3):
  return lambda z18: (lambda x0, x1, x2: ['-',x0,x2])(z18, x0, x3(x2(x1)))

def expansion_29(x0, x1, x2):
  return lambda z9: (lambda x0, x1, x2: ['/',x0,x2])(z9, x0, x2(x1))

def expansion_35(x0, x1, x2, x3):
  return lambda z4: (lambda x0, x1, x2, x3: ['funcall',x0.symbolic_name,x2])(z4, x0, x2(x1), x3)

def expansion_37(x0, x1, x2):
  return (x2(x1))(x0)

def expansion_41(x0, x1):
  return (lambda x0, x1: -x1)(x0, x1)

def expansion_42(x0):
  return (lambda x0: x0)(x0)

def expansion_43(x0):
  return (lambda x0: x0.val())(x0)

def expansion_44(x0, x1, x2, x3, x4):
  return (lambda x0, x1, x2: ['group',x1])(x0, x3(x2(x1)), x4)

def expansion_49(x0, x1, x2):
  return lambda z25: (lambda x0, x1, x2: ['*',x0,x2])(z25, x0, x2(x1))

def expansion_50(x0, x1):
  return lambda z23: (lambda x0: x0)((lambda x0, x1, x2: ['range',x0,x2])(z23, x0, x1))

def expansion_52(x0, x1):
  return lambda z16: (lambda x0, x1, x2: parse_cellref(['cellref',x0.symbolic_name,'ABS',str(int(x2))]))(z16, x0, x1)

def expansion_53(x0, x1):
  return lambda z7: lambda z6: (lambda x0, x1, x2, x3: parse_cellref(['cellref','ABS',x1.symbolic_name,'ABS',str(int(x3))]))(z6, z7, x0, x1)

def expansion_54(x0, x1, x2):
  return lambda z1: (lambda x0, x1, x2: [x0]+x2)(z1, x0, x2(x1))

def expansion_56(x0, x1, x2, x3, x4, x5):
  return ((x5(x4(x3(x2))))(x1))(x0)

def expansion_57(x0, x1, x2):
  return (lambda x0: x0)(x2(x1(x0)))

def expr_3():
  return lambda _yyy: (lambda x0: x0)(_yyy)

def list_10_12_25():
  return lambda _yyy: lambda z39: lambda z8: (lambda x0: [x0])((lambda x0, x1, x2: (x0,x2))(z8, z39, _yyy))

def list_10_12_25_37_1():
  return lambda _yyy: lambda z29: lambda z22: lambda z2: (lambda x0, x1: [x0])((lambda x0, x1, x2: (x0,x2))(z2, z22, z29), _yyy)

def new_calculated_action_2(first, continuation):
  return continuation(first)

def new_expansion_0(first, continuation):
  return continuation(first)

def new_list_10_12_25_1(first, continuation):
  return continuation(first)

def term_0():
  return lambda _yyy: (lambda x0: x0)(_yyy)


