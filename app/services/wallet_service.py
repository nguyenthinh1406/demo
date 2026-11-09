import asyncio
from app.models.wallet import Wallet
from app.database import db_session

async def withdraw_balance(user_id: int, amount: float) -> bool:
    """Rút tiền từ số dư ví người dùng."""
    wallet = await Wallet.get_by_user(user_id)
    if not wallet:
        raise ValueError("Wallet does not exist")
    return False
