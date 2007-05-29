
import aperiot.lexer


# Non-terminal symbol names

CALCULATED_4_15 = 'CALCULATED_4_15'
CALCULATED = 'CALCULATED'
ARGLIST_11 = 'ARGLIST_11'
LIST_10_12_25 = 'LIST_10_12_25'
CALCULATED_5 = 'CALCULATED_5'
FACTOR = 'FACTOR'
LIST_10_12_25_37 = 'LIST_10_12_25_37'
LIST = 'LIST'
EXPR_3 = 'EXPR_3'
TERM_0 = 'TERM_0'
ARG = 'ARG'
ARG_1 = 'ARG_1'

rules = \
  {
    CALCULATED_4_15: 
      [
        ([], 'calculated_4_15'),
        ([Operator('$', 'absolute'), aperiot.lexer.NumberLiteral], 'expansion_53'),
      ], 
    CALCULATED: 
      [
        ([Operator('$', 'absolute'), aperiot.lexer.Identifier, CALCULATED_4_15], 'expansion_37'),
        ([aperiot.lexer.Identifier, CALCULATED_5], 'new_calculated_action_2'),
      ], 
    ARGLIST_11: 
      [
        ([Operator(',', 'comma'), ARG, ARGLIST_11], 'expansion_54'),
        ([], 'arglist_11_1'),
      ], 
    LIST_10_12_25: 
      [
        ([], 'list_10_12_25'),
        ([Operator(';', 'semicolon'), LIST_10_12_25_37], 'new_list_10_12_25_1'),
      ], 
    CALCULATED_5: 
      [
        ([Operator('$', 'absolute'), aperiot.lexer.NumberLiteral], 'expansion_52'),
        ([], 'calculated_5_1'),
        ([Bracket('(', 'lpar'), ARG, ARGLIST_11, Bracket(')', 'rpar')], 'expansion_35'),
      ], 
    FACTOR: 
      [
        ([aperiot.lexer.NumberLiteral], 'expansion_43'),
        ([Bracket('(', 'lpar'), FACTOR, TERM_0, EXPR_3, Bracket(')', 'rpar')], 'expansion_44'),
        ([Operator('-', 'minus'), FACTOR], 'expansion_41'),
        ([CALCULATED], 'expansion_42'),
      ], 
    LIST_10_12_25_37: 
      [
        ([LIST], 'expansion_13'),
        ([], 'list_10_12_25_37_1'),
      ], 
    LIST: 
      [
        ([aperiot.lexer.Identifier, Operator('=', 'equal'), FACTOR, TERM_0, EXPR_3, LIST_10_12_25], 'expansion_56'),
      ], 
    EXPR_3: 
      [
        ([], 'expr_3'),
        ([Operator('+', 'plus'), FACTOR, TERM_0, EXPR_3], 'expansion_26'),
        ([Operator('-', 'minus'), FACTOR, TERM_0, EXPR_3], 'expansion_27'),
      ], 
    TERM_0: 
      [
        ([], 'term_0'),
        ([Operator('*', 'times'), FACTOR, TERM_0], 'expansion_49'),
        ([Operator('/', 'div'), FACTOR, TERM_0], 'expansion_29'),
      ], 
    ARG: 
      [
        ([CALCULATED, ARG_1], 'new_expansion_0'),
        ([FACTOR, TERM_0, EXPR_3], 'expansion_57'),
      ], 
    ARG_1: 
      [
        ([Operator(':', 'colon'), CALCULATED], 'expansion_50'),
        ([], 'arg_1_1'),
      ], 
  }

start = LIST


