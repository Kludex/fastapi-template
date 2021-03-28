from fastapi import APIRouter

router = APIRouter(tags=["Home"])


@router.get("/")
async def home():
    """Home endpoint."""
    return {"Hello": "World!"}
