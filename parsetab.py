
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND DIVIDE EQ GT GTE ID LPAREN LT LTE MINUS NEQ NOT NUMBER OR PLUS RPAREN TIMES comma semiCollumEXP : PARAMETRO EXP_L1\n           | LPAREN PARAMETRO EXP_L2 RPAREN PARAMETRO : IDempty : semiCollum \n             | RPAREN EXP_L1 : EXP OP_LOGICO EXP\n              | emptyEXP_L2 : EXP OP_MAT EXP\n              | emptyPARAM_LOGICO : EXP_LOGICO\n                    | OP_LOGICO EXP\n                    | PARAM_LOGICO comma EXP_LOGICOEXP_LOGICO : OP_LOGICO EXP\n                  | emptyOP_MAT : PLUS\n              | MINUS\n              | TIMES\n              | DIVIDEOP_LOGICO : AND\n                 | OR\n                 | NOTOP_COMP : EQ\n               | NEQ\n               | LT\n               | GT\n               | LTE\n               | GTE'
    
_lr_action_items = {'LPAREN':([0,2,4,10,11,12,13,14,20,21,22,23,24,],[3,3,-3,3,3,-19,-20,-21,3,-15,-16,-17,-18,]),'ID':([0,2,3,4,10,11,12,13,14,20,21,22,23,24,],[4,4,4,-3,4,4,-19,-20,-21,4,-15,-16,-17,-18,]),'$end':([1,5,7,8,9,18,19,],[0,-1,-7,-5,-4,-6,-2,]),'semiCollum':([2,4,10,],[9,-3,9,]),'RPAREN':([2,4,5,7,8,9,10,15,17,18,19,25,],[8,-3,-1,-7,-5,-4,8,19,-9,-6,-2,-8,]),'AND':([5,6,7,8,9,18,19,],[-1,12,-7,-5,-4,-6,-2,]),'OR':([5,6,7,8,9,18,19,],[-1,13,-7,-5,-4,-6,-2,]),'NOT':([5,6,7,8,9,18,19,],[-1,14,-7,-5,-4,-6,-2,]),'PLUS':([5,7,8,9,16,18,19,],[-1,-7,-5,-4,21,-6,-2,]),'MINUS':([5,7,8,9,16,18,19,],[-1,-7,-5,-4,22,-6,-2,]),'TIMES':([5,7,8,9,16,18,19,],[-1,-7,-5,-4,23,-6,-2,]),'DIVIDE':([5,7,8,9,16,18,19,],[-1,-7,-5,-4,24,-6,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'EXP':([0,2,10,11,20,],[1,6,16,18,25,]),'PARAMETRO':([0,2,3,10,11,20,],[2,2,10,2,2,2,]),'EXP_L1':([2,],[5,]),'empty':([2,10,],[7,17,]),'OP_LOGICO':([6,],[11,]),'EXP_L2':([10,],[15,]),'OP_MAT':([16,],[20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> EXP","S'",1,None,None,None),
  ('EXP -> PARAMETRO EXP_L1','EXP',2,'p_exp','ps_sintatico.py',13),
  ('EXP -> LPAREN PARAMETRO EXP_L2 RPAREN','EXP',4,'p_exp','ps_sintatico.py',14),
  ('PARAMETRO -> ID','PARAMETRO',1,'p_parametro','ps_sintatico.py',17),
  ('empty -> semiCollum','empty',1,'p_empty','ps_sintatico.py',19),
  ('empty -> RPAREN','empty',1,'p_empty','ps_sintatico.py',20),
  ('EXP_L1 -> EXP OP_LOGICO EXP','EXP_L1',3,'p_exp_l1','ps_sintatico.py',22),
  ('EXP_L1 -> empty','EXP_L1',1,'p_exp_l1','ps_sintatico.py',23),
  ('EXP_L2 -> EXP OP_MAT EXP','EXP_L2',3,'p_exp_l2','ps_sintatico.py',28),
  ('EXP_L2 -> empty','EXP_L2',1,'p_exp_l2','ps_sintatico.py',29),
  ('PARAM_LOGICO -> EXP_LOGICO','PARAM_LOGICO',1,'p_param_logico','ps_sintatico.py',34),
  ('PARAM_LOGICO -> OP_LOGICO EXP','PARAM_LOGICO',2,'p_param_logico','ps_sintatico.py',35),
  ('PARAM_LOGICO -> PARAM_LOGICO comma EXP_LOGICO','PARAM_LOGICO',3,'p_param_logico','ps_sintatico.py',36),
  ('EXP_LOGICO -> OP_LOGICO EXP','EXP_LOGICO',2,'p_exp_logico','ps_sintatico.py',40),
  ('EXP_LOGICO -> empty','EXP_LOGICO',1,'p_exp_logico','ps_sintatico.py',41),
  ('OP_MAT -> PLUS','OP_MAT',1,'p_op_mat','ps_sintatico.py',46),
  ('OP_MAT -> MINUS','OP_MAT',1,'p_op_mat','ps_sintatico.py',47),
  ('OP_MAT -> TIMES','OP_MAT',1,'p_op_mat','ps_sintatico.py',48),
  ('OP_MAT -> DIVIDE','OP_MAT',1,'p_op_mat','ps_sintatico.py',49),
  ('OP_LOGICO -> AND','OP_LOGICO',1,'p_op_logico','ps_sintatico.py',53),
  ('OP_LOGICO -> OR','OP_LOGICO',1,'p_op_logico','ps_sintatico.py',54),
  ('OP_LOGICO -> NOT','OP_LOGICO',1,'p_op_logico','ps_sintatico.py',55),
  ('OP_COMP -> EQ','OP_COMP',1,'p_op_comp','ps_sintatico.py',59),
  ('OP_COMP -> NEQ','OP_COMP',1,'p_op_comp','ps_sintatico.py',60),
  ('OP_COMP -> LT','OP_COMP',1,'p_op_comp','ps_sintatico.py',61),
  ('OP_COMP -> GT','OP_COMP',1,'p_op_comp','ps_sintatico.py',62),
  ('OP_COMP -> LTE','OP_COMP',1,'p_op_comp','ps_sintatico.py',63),
  ('OP_COMP -> GTE','OP_COMP',1,'p_op_comp','ps_sintatico.py',64),
]
