from typing import NamedTuple, Tuple, List
from . import ast

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path  # type: ignore

# Target python version
CompilationTarget = Tuple[int, int]

# Information about compilation
CompilationResult = NamedTuple('CompilationResult',
                               [('files', int),
                                ('time', float),
                                ('target', CompilationTarget),
                                ('dependencies', List[str])])

# Input/output pair
InputOutput = NamedTuple('InputOutput', [('input', Path),
                                         ('output', Path)])

# Result of transformers transformation
TransformationResult = NamedTuple('TransformationResult',
                                  [('tree', ast.AST),
                                   ('tree_changed', bool),
                                   ('dependencies', List[str])])

# Node position in tree:
NodePosition = NamedTuple('NodePosition',
                          [('parent', ast.AST),
                           ('attribute', str),
                           ('holder', List[ast.AST]),
                           ('index', int)])
