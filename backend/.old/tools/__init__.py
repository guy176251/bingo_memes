from pprint import pformat

from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer


def pprint_color(obj):
    print(highlight(pformat(obj, indent=2), PythonLexer(), Terminal256Formatter()))
