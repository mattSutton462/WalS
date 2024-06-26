
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSrightPOWERnonassocEQNEQLTLTEGTGTEleftANDleftORrightNOTAND ASSIGN DECREMENT DIVIDE ELSE EQ FOR GT GTE ID IF INCREMENT LPAREN LT LTE MINUS NEQ NOT NUMBER OR PLUS POWER PRINT RPAREN TIMES WHILEstatement : statement : expression\n                 | PRINT LPAREN expression RPARENexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression POWER expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBERexpression : IDexpression : ID ASSIGN expressionexpression : ID INCREMENT\n                  | ID DECREMENT'
    
_lr_action_items = {'$end':([0,1,2,6,7,15,17,18,19,20,21,22,23,25,26,27,],[-1,0,-2,-11,-12,-9,-14,-15,-4,-5,-6,-7,-8,-10,-13,-3,]),'PRINT':([0,],[3,]),'MINUS':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[5,9,5,5,-11,-12,5,5,5,5,5,5,9,-9,5,-14,-15,-4,-5,-6,-7,-8,9,-10,9,]),'LPAREN':([0,3,4,5,8,9,10,11,12,13,16,],[4,13,4,4,4,4,4,4,4,4,4,]),'NUMBER':([0,4,5,8,9,10,11,12,13,16,],[6,6,6,6,6,6,6,6,6,6,]),'ID':([0,4,5,8,9,10,11,12,13,16,],[7,7,7,7,7,7,7,7,7,7,]),'PLUS':([2,6,7,14,15,17,18,19,20,21,22,23,24,25,26,],[8,-11,-12,8,-9,-14,-15,-4,-5,-6,-7,-8,8,-10,8,]),'TIMES':([2,6,7,14,15,17,18,19,20,21,22,23,24,25,26,],[10,-11,-12,10,-9,-14,-15,10,10,-6,-7,-8,10,-10,10,]),'DIVIDE':([2,6,7,14,15,17,18,19,20,21,22,23,24,25,26,],[11,-11,-12,11,-9,-14,-15,11,11,-6,-7,-8,11,-10,11,]),'POWER':([2,6,7,14,15,17,18,19,20,21,22,23,24,25,26,],[12,-11,-12,12,12,-14,-15,12,12,12,12,12,12,-10,12,]),'RPAREN':([6,7,14,15,17,18,19,20,21,22,23,24,25,26,],[-11,-12,25,-9,-14,-15,-4,-5,-6,-7,-8,27,-10,-13,]),'ASSIGN':([7,],[16,]),'INCREMENT':([7,],[17,]),'DECREMENT':([7,],[18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,8,9,10,11,12,13,16,],[2,14,15,19,20,21,22,23,24,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> <empty>','statement',0,'p_statement_empty','WalS_Abstract_Syntax_Tree.py',88),
  ('statement -> expression','statement',1,'p_statement_expr','WalS_Abstract_Syntax_Tree.py',93),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement_expr','WalS_Abstract_Syntax_Tree.py',94),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','WalS_Abstract_Syntax_Tree.py',101),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','WalS_Abstract_Syntax_Tree.py',102),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','WalS_Abstract_Syntax_Tree.py',103),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','WalS_Abstract_Syntax_Tree.py',104),
  ('expression -> expression POWER expression','expression',3,'p_expression_binop','WalS_Abstract_Syntax_Tree.py',105),
  ('expression -> MINUS expression','expression',2,'p_expression_unary_minus','WalS_Abstract_Syntax_Tree.py',109),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','WalS_Abstract_Syntax_Tree.py',113),
  ('expression -> NUMBER','expression',1,'p_expression_number','WalS_Abstract_Syntax_Tree.py',117),
  ('expression -> ID','expression',1,'p_expression_id','WalS_Abstract_Syntax_Tree.py',121),
  ('expression -> ID ASSIGN expression','expression',3,'p_expression_assignment','WalS_Abstract_Syntax_Tree.py',125),
  ('expression -> ID INCREMENT','expression',2,'p_expression_increment_decrement','WalS_Abstract_Syntax_Tree.py',129),
  ('expression -> ID DECREMENT','expression',2,'p_expression_increment_decrement','WalS_Abstract_Syntax_Tree.py',130),
]
