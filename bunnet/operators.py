from bunnet.odm.operators.find.array import All, ElemMatch, Size
from bunnet.odm.operators.find.bitwise import (
    BitsAllClear,
    BitsAllSet,
    BitsAnyClear,
    BitsAnySet,
)
from bunnet.odm.operators.find.comparison import (
    Eq,
    GT,
    GTE,
    In,
    NotIn,
    LT,
    LTE,
    NE,
)
from bunnet.odm.operators.find.element import Exists, Type
from bunnet.odm.operators.find.evaluation import (
    Expr,
    JsonSchema,
    Mod,
    RegEx,
    Text,
    Where,
)
from bunnet.odm.operators.find.geospatial import (
    GeoIntersects,
    GeoWithinTypes,
    GeoWithin,
    Near,
    NearSphere,
)
from bunnet.odm.operators.find.logical import Or, And, Nor, Not
from bunnet.odm.operators.update.array import (
    AddToSet,
    Pop,
    Pull,
    Push,
    PullAll,
)
from bunnet.odm.operators.update.bitwise import Bit
from bunnet.odm.operators.update.general import (
    Set,
    CurrentDate,
    Inc,
    Min,
    Max,
    Mul,
    Rename,
    SetOnInsert,
    Unset,
)

__all__ = [
    # Find
    # Array
    "All",
    "ElemMatch",
    "Size",
    # Bitwise
    "BitsAllClear",
    "BitsAllSet",
    "BitsAnyClear",
    "BitsAnySet",
    # Comparison
    "Eq",
    "GT",
    "GTE",
    "In",
    "NotIn",
    "LT",
    "LTE",
    "NE",
    # Element
    "Exists",
    "Type",
    "Type",
    # Evaluation
    "Expr",
    "JsonSchema",
    "Mod",
    "RegEx",
    "Text",
    "Where",
    # Geospatial
    "GeoIntersects",
    "GeoWithinTypes",
    "GeoWithin",
    "Near",
    "NearSphere",
    # Logical
    "Or",
    "And",
    "Nor",
    "Not",
    # Update
    # Array
    "AddToSet",
    "Pop",
    "Pull",
    "Push",
    "PullAll",
    # Bitwise
    "Bit",
    # General
    "Set",
    "CurrentDate",
    "Inc",
    "Min",
    "Max",
    "Mul",
    "Rename",
    "SetOnInsert",
    "Unset",
]
