from uuid import uuid4
from time import perf_counter
from functools import wraps
from bisect import bisect_left

hexnames = [
    "black",
    "navy",
    "darkblue",
    "mediumblue",
    "blue",
    "darkgreen",
    "green",
    "teal",
    "darkcyan",
    "deepskyblue",
    "darkturquoise",
    "mediumspringgreen",
    "lime",
    "springgreen",
    "cyan",
    "midnightblue",
    "dodgerblue",
    "lightseagreen",
    "forestgreen",
    "seagreen",
    "darkslategray",
    "limegreen",
    "mediumseagreen",
    "turquoise",
    "royalblue",
    "steelblue",
    "darkslateblue",
    "mediumturquoise",
    "indigo",
    "darkolivegreen",
    "cadetblue",
    "cornflowerblue",
    "mediumaquamarine",
    "dimgray",
    "slateblue",
    "olivedrab",
    "slategray",
    "lightslategray",
    "mediumslateblue",
    "lawngreen",
    "chartreuse",
    "aquamarine",
    "maroon",
    "purple",
    "olive",
    "gray",
    "skyblue",
    "lightskyblue",
    "blueviolet",
    "darkred",
    "darkmagenta",
    "saddlebrown",
    "darkseagreen",
    "lightgreen",
    "mediumpurple",
    "darkviolet",
    "palegreen",
    "darkorchid",
    "yellowgreen",
    "sienna",
    "brown",
    "darkgray",
    "lightblue",
    "greenyellow",
    "paleturquoise",
    "lightsteelblue",
    "powderblue",
    "firebrick",
    "darkgoldenrod",
    "mediumorchid",
    "rosybrown",
    "darkkhaki",
    "silver",
    "mediumvioletred",
    "indianred",
    "peru",
    "chocolate",
    "tan",
    "lightgray",
    "thistle",
    "orchid",
    "goldenrod",
    "palevioletred",
    "crimson",
    "gainsboro",
    "plum",
    "burlywood",
    "lightcyan",
    "lavender",
    "darksalmon",
    "violet",
    "palegoldenrod",
    "lightcoral",
    "khaki",
    "aliceblue",
    "honeydew",
    "azure",
    "sandybrown",
    "wheat",
    "beige",
    "whitesmoke",
    "mintcream",
    "ghostwhite",
    "salmon",
    "antiquewhite",
    "linen",
    "lightgoldenrodyellow",
    "oldlace",
    "red",
    "magenta",
    "deeppink",
    "orangered",
    "tomato",
    "hotpink",
    "coral",
    "darkorange",
    "lightsalmon",
    "orange",
    "lightpink",
    "pink",
    "gold",
    "peachpuff",
    "navajowhite",
    "moccasin",
    "bisque",
    "mistyrose",
    "blanchedalmond",
    "papayawhip",
    "lavenderblush",
    "seashell",
    "cornsilk",
    "lemonchiffon",
    "floralwhite",
    "snow",
    "yellow",
    "lightyellow",
    "ivory",
    "white",
]

hexvalues = [
    0,
    128,
    139,
    205,
    255,
    25600,
    32768,
    32896,
    35723,
    49151,
    52945,
    64154,
    65280,
    65407,
    65535,
    1644912,
    2003199,
    2142890,
    2263842,
    3050327,
    3100495,
    3329330,
    3978097,
    4251856,
    4286945,
    4620980,
    4734347,
    4772300,
    4915330,
    5597999,
    6266528,
    6591981,
    6737322,
    6908265,
    6970061,
    7048739,
    7372944,
    7833753,
    8087790,
    8190976,
    8388352,
    8388564,
    8388608,
    8388736,
    8421376,
    8421504,
    8900331,
    8900346,
    9055202,
    9109504,
    9109643,
    9127187,
    9419919,
    9498256,
    9662683,
    9699539,
    10025880,
    10040012,
    10145074,
    10506797,
    10824234,
    11119017,
    11393254,
    11403055,
    11529966,
    11584734,
    11591910,
    11674146,
    12092939,
    12211667,
    12357519,
    12433259,
    12632256,
    13047173,
    13458524,
    13468991,
    13789470,
    13808780,
    13882323,
    14204888,
    14315734,
    14329120,
    14381203,
    14423100,
    14474460,
    14524637,
    14596231,
    14745599,
    15132410,
    15308410,
    15631086,
    15657130,
    15761536,
    15787660,
    15792383,
    15794160,
    15794175,
    16032864,
    16113331,
    16119260,
    16119285,
    16121850,
    16316671,
    16416882,
    16444375,
    16445670,
    16448210,
    16643558,
    16711680,
    16711935,
    16716947,
    16729344,
    16737095,
    16738740,
    16744272,
    16747520,
    16752762,
    16753920,
    16758465,
    16761035,
    16766720,
    16767673,
    16768685,
    16770229,
    16770244,
    16770273,
    16772045,
    16773077,
    16773365,
    16774638,
    16775388,
    16775885,
    16775920,
    16775930,
    16776960,
    16777184,
    16777200,
    16777215,
]


def getID():
    return int(uuid4())


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = perf_counter()
        result = f(*args, **kw)
        te = perf_counter()
        print(f"function: {f.__name__} took: {te-ts:2.5e} sec.")
        return result

    return wrap


def hex2name(hexvalue):
    if hexvalue == 'none':
        return 'white'

    hexvalue = int(hexvalue[1:], 16)
    idx = bisect_left(hexvalues, hexvalue)
    return hexnames[idx]


if __name__ == "__main__":

    print(hex2name2("#B22223"))
