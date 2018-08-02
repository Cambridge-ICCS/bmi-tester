from .utils import all_names, all_grids


VALID_GRID_TYPES = (
    "scalar",
    "vector",
    "unstructured",
    "unstructured_triangular",
    "rectilinear",
    "structured_quadrilateral",
    "uniform_rectilinear",
    "uniform_rectilinear_grid",
)


def test_valid_grid_rank(new_bmi, gid):
    "Test grid rank for grid {gid}".format(gid=gid)
    rank = new_bmi.get_grid_rank(gid)
    assert isinstance(rank, int)
    assert rank <= 3


def test_get_grid_size(new_bmi, gid):
    "Test grid size for grid {gid}".format(gid=gid)
    size = new_bmi.get_grid_size(gid)
    assert isinstance(size, int)
    assert size > 0


def test_get_grid_type(new_bmi, gid):
    "Test grid is known for grid {gid}".format(gid=gid)
    gtype = new_bmi.get_grid_type(gid)
    assert isinstance(gtype, str)
    assert gtype in VALID_GRID_TYPES
    if gtype == "scalar":
        assert new_bmi.get_grid_rank(gid) == 0
