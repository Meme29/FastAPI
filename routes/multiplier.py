from fastapi import APIRouter

router = APIRouter()

@router.get("/multiplier/{x}", tags=["Multiplier"])
def get_products(x: float):
    return {"result": x * 2}