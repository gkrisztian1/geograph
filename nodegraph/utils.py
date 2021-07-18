from typing import Iterable
from uuid import uuid4
from time import perf_counter
from functools import wraps
from bisect import bisect_left
import numpy as np

default_color = "none"

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
    if hexvalue == "none":
        return "white"

    hexvalue = int(hexvalue[1:], 16)
    idx = bisect_left(hexvalues, hexvalue)
    return hexnames[idx]


def is_rectangle_intersect(r1: Iterable, r2: Iterable):

    r1_left, r1_bottom, r1_right, r1_top = r1
    r2_left, r2_bottom, r2_right, r2_top = r2

    assert r1_left <= r1_right, f"Not a proper bounding box: {r1}"
    assert r2_left <= r2_right, f"Not a proper bounding box: {r2}"
    assert r1_bottom <= r1_top, f"Not a proper bounding box: {r1}"
    assert r2_bottom <= r2_top, f"Not a proper bounding box: {r2}"

    return not (
        (r2_left > r1_right)
        or (r2_right < r1_left)
        or (r2_top < r1_bottom)
        or (r2_bottom > r1_top)
    )


def get_intersections(p1x, p1y, q1x, q1y, p2x, p2y, q2x, q2y, epsilon=1e-3):
    """
    :param line_1: the first line
    :param line_2: second line
    :returns: () or ((x, y)) or ((x1, y1), (x2, y2))
    https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
    Conditions:
    1. If r × s = 0 and (q − p) × r = 0, then the two lines are collinear.
    2. If r × s = 0 and (q − p) × r ≠ 0, then the two lines are parallel and non-intersecting.
    3. If r × s ≠ 0 and 0 ≤ t ≤ 1 and 0 ≤ u ≤ 1, the two line segments meet at the point p + t r = q + u s.
    4. Otherwise, the two line segments are not parallel but do not intersect.
    """

    intersection_points = list()
    p1 = None
    p2 = None

    p = np.array([p1x, p1y])
    r = np.array([q1x - p1x, q1y - p1y])

    q = np.array([p2x, p2y])
    s = np.array([q2x - p2x, q2y - p2y])

    test1 = np.abs(np.cross(r, s))
    test2 = np.abs(np.cross((q - p), r))

    t0 = np.dot(q - p, r) / np.dot(r, r)
    t1 = t0 + np.dot(s, r) / np.dot(r, r)
    t2 = np.dot(p - q, s) / np.dot(s, s)
    t3 = t2 + np.dot(r, s) / np.dot(s, s)

    inrange = lambda x: x > (0 - epsilon) and x < (1 + epsilon)
    distance = lambda x, y: np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

    if test1 < epsilon:

        if test2 < epsilon:

            if inrange(t0):
                p1 = tuple(p + t0 * r)

            if inrange(t1):
                p2 = tuple(p + t1 * r)

            if inrange(t2):
                p1 = tuple(q + t2 * s)

            if inrange(t3):
                p2 = tuple(q + t3 * s)

    else:
        up = (
            -p1x * q1y + p1x * p2y + q1x * p1y - q1x * p2y - p2x * p1y + p2x * q1y
        ) / (
            p1x * p2y
            - p1x * q2y
            - q1x * p2y
            + q1x * q2y
            - p2x * p1y
            + p2x * q1y
            + q2x * p1y
            - q2x * q1y
        )
        tp = (p1x * p2y - p1x * q2y - p2x * p1y + p2x * q2y + q2x * p1y - q2x * p2y) / (
            p1x * p2y
            - p1x * q2y
            - q1x * p2y
            + q1x * q2y
            - p2x * p1y
            + p2x * q1y
            + q2x * p1y
            - q2x * q1y
        )
        if inrange(tp) and inrange(up):
            p1 = tuple(p + tp * r)

    if (p1 is not None) and (p2 is not None) and (distance(p1, p2) < epsilon):
        p2 = None

    if p1 is not None:
        intersection_points.append(p1)

    if p2 is not None:
        intersection_points.append(p2)

    return intersection_points

    return intersection_points
