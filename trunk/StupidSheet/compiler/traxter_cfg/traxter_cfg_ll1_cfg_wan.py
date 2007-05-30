
import aperiot.lexer


# Non-terminal symbol names

CALCULATED_4_15 = 'CALCULATED_4_15'
ARGLIST_12 = 'ARGLIST_12'
CALCULATED = 'CALCULATED'
CALCULATED_5 = 'CALCULATED_5'
FACTOR = 'FACTOR'
LIST_11_17_27_38 = 'LIST_11_17_27_38'
LIST = 'LIST'
ARG_1 = 'ARG_1'
TERM_0 = 'TERM_0'
LIST_11_17_27 = 'LIST_11_17_27'
ARG = 'ARG'
EXPR_3 = 'EXPR_3'

rules = \
  {
    CALCULATED_4_15: 
      [
        ([], 'calculated_4_15'),
        ([Operator('$', 'absolute'), aperiot.lexer.NumberLiteral], 'expansion_51'),
      ], 
    ARGLIST_12: 
      [
        ([Operator(',', 'comma'), ARG, ARGLIST_12], 'expansion_49'),
        ([], 'arglist_12_1'),
      ], 
    CALCULATED: 
      [
        ([Operator('$', 'absolute'), aperiot.lexer.Identifier, CALCULATED_4_15], 'expansion_41'),
        ([aperiot.lexer.Identifier, CALCULATED_5], 'new_calculated_action_2'),
      ], 
    CALCULATED_5: 
      [
        ([Operator('$', 'absolute'), aperiot.lexer.NumberLiteral], 'expansion_39'),
        ([], 'calculated_5_1'),
        ([Bracket('(', 'lpar'), ARG, ARGLIST_12, Bracket(')', 'rpar')], 'expansion_44'),
      ], 
    FACTOR: 
      [
        ([aperiot.lexer.NumberLiteral], 'expansion_47'),
        ([Bracket('(', 'lpar'), FACTOR, TERM_0, EXPR_3, Bracket(')', 'rpar')], 'expansion_48'),
        ([Operator('-', 'minus'), FACTOR], 'expansion_45'),
        ([CALCULATED], 'expansion_46'),
        ([aperiot.lexer.StringLiteral], 'expansion_10'),
      ], 
    LIST_11_17_27_38: 
      [
        ([LIST], 'expansion_11'),
        ([], 'list_11_17_27_38_1'),
      ], 
    LIST: 
      [
        ([aperiot.lexer.Identifier, Operator('=', 'equal'), FACTOR, TERM_0, EXPR_3, LIST_11_17_27], 'expansion_55'),
      ], 
    ARG_1: 
      [
        ([Operator(':', 'colon'), CALCULATED], 'expansion_56'),
        ([], 'arg_1_1'),
      ], 
    TERM_0: 
      [
        ([], 'term_0'),
        ([Operator('*', 'times'), FACTOR, TERM_0], 'expansion_30'),
        ([Operator('/', 'div'), FACTOR, TERM_0], 'expansion_29'),
      ], 
    LIST_11_17_27: 
      [
        ([], 'list_11_17_27'),
        ([Operator(';', 'semicolon'), LIST_11_17_27_38], 'new_list_11_17_27_1'),
      ], 
    ARG: 
      [
        ([CALCULATED, ARG_1], 'new_expansion_0'),
        ([FACTOR, TERM_0, EXPR_3], 'expansion_58'),
      ], 
    EXPR_3: 
      [
        ([], 'expr_3'),
        ([Operator('+', 'plus'), FACTOR, TERM_0, EXPR_3], 'expansion_27'),
        ([Operator('-', 'minus'), FACTOR, TERM_0, EXPR_3], 'expansion_28'),
      ], 
  }

start = LIST


