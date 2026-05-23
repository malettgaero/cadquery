"""CadQuery - A parametric 3D CAD scripting framework.

CadQuery is an intuitive, easy-to-use Python module for building parametric
3D CAD models. It is modeled after OpenSCAD, but uses a different approach
to constructing models, and uses Python as the scripting language.

Example usage::

    import cadquery as cq

    # Create a simple box
    result = cq.Workplane("XY").box(10, 10, 5)

    # Export to STEP
    cq.exporters.export(result, "box.step")

Useful links:
    - Documentation: https://cadquery.readthedocs.io
    - GitHub: https://github.com/CadQuery/cadquery
    - Examples: https://github.com/CadQuery/cadquery/tree/master/examples
"""

from .cq import Workplane, CQContext
from .occ_impl.geom import Vector, Matrix, Plane, BoundBox
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
    CompSolid,
)
from .assembly import Assembly, ConstraintKind
from .sketch import Sketch
from . import exporters
from . import importers
from . import selectors
from .selectors import (
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    CenterNthSelector,
    RadiusNthSelector,
    LengthNthSelector,
    DirectionNthSelector,
    AndSelector,
    SumSelector,
    SubtractSelector,
    InverseSelector,
    BoxSelector,
    BaseDirSelector,
    StringSyntaxSelector,
)
from .cq_selectors import Selector

__version__ = "2.5.0.dev0"
__author__ = "CadQuery Contributors"
__license__ = "Apache License 2.0"

__all__ = [
    # Core workplane
    "Workplane",
    "CQContext",
    # Geometry primitives
    "Vector",
    "Matrix",
    "Plane",
    "BoundBox",
    # Shapes
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    "CompSolid",
    # Assembly
    "Assembly",
    "ConstraintKind",
    # Sketch
    "Sketch",
    # Modules
    "exporters",
    "importers",
    "selectors",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "DirectionMinMaxSelector",
    "CenterNthSelector",
    "RadiusNthSelector",
    "LengthNthSelector",
    "DirectionNthSelector",
    "AndSelector",
    "SumSelector",
    "SubtractSelector",
    "InverseSelector",
    "BoxSelector",
    "BaseDirSelector",
    "StringSyntaxSelector",
    # Version info
    "__version__",
]
