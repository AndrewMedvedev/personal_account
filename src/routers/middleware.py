from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter


limiter = Limiter(key_func=get_remote_address, default_limits=["10/second"])
router = APIRouter()
router.state.limiter = limiter
router.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
router.add_middleware(SlowAPIMiddleware)

router.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
