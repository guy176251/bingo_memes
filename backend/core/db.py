from django.db.models import Func


class Log10(Func):
    function = "LOG10"


class Sign(Func):
    function = "SIGN"


class Abs(Func):
    function = "ABS"


class Sqrt(Func):
    function = "SQRT"


class Mod(Func):
    function = "MOD"
