from fastapi import APIRouter
from backend.schemas.request_schema import BenchmarkRequest
from utils.parser import parse_input
from utils.benchmark import run_benchmark

router = APIRouter(prefix="/benchmark", tags=["benchmark"])

@router.post("/")
def run_dsa_benchmark(req:BenchmarkRequest):
    parsed = parse_input(req.raw_input)
    module = parsed.get("module")
    operation = parsed.get("operation")

    if module is None:
        return {

            "erroer":"Could not detect module from input", 
            "parsed":parsed 
        }
    

    result = run_benchmark(module, operation)
    return {
        "parsed":parsed,
        "benchmark":result
    }