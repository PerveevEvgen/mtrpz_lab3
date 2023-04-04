import numpy
from fastapi import APIRouter

router = APIRouter()

@router.get('/matrix')
def matrix() -> dict:
    mtr_a = numpy.random.rand(10, 10)
    mtr_b = numpy.random.rand(10, 10)
    res_mtr = numpy.dot(mtr_a, mtr_b)

    result = {
        "mtr_a": mtr_a.tolist(),
        "mtr_b": mtr_b.tolist(),
        "res_mtr": res_mtr.tolist()
    }

    return result