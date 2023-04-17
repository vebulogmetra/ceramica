from sqlalchemy.ext.asyncio import AsyncSession
from db.models import User



class UserCRUD:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create(self, username: str, name: str, surname: str, email: str) -> User:
        new_user = User(username=username, name=name, surname=surname, email=email,)
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user