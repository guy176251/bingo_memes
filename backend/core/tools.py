from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter
from pprint import pformat


def pprint_color(obj):
    print(highlight(pformat(obj, indent=2), PythonLexer(), Terminal256Formatter()))
