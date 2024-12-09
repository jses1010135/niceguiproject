from model.user_account_model import UserAccount #workflows 資料運算
from init_db import get_async_session_context
from sqlalchemy.future import select
from typing import List

class UserAccountControler:

    @staticmethod#宣告類別方法
    async def add_user_account(account: str, email: str, password: str, address: str) -> None:
        async with get_async_session_context() as session:  #get_async_session_context() 建立資料庫連線 #session:資料庫連線      
            user_account = UserAccount(#UserAccount:資料表 
                account = account,
                email = email,
                password = password,
                address = address
            )
            session.add(user_account)#將資料加入資料庫
            await session.commit()#await:等待資料庫操作完成 #commit:確認資料庫操作 #async:非同步函數
            return user_account
        
    @staticmethod
    async def delete_user_account(id: int = None, account: str = None, email: str = None) -> None:
        async with get_async_session_context() as session:
            result = await session.execute(
                select(UserAccount).where((UserAccount.id == id) | (UserAccount.account == account) | (UserAccount.email == email))
            )
            user_account = result.scalars().first()
            await session.delete(user_account)
            await session.commit()

    @staticmethod
    async def update_user_account(id: int, account: str = None, email: str = None, password: str = None, address: str = None) -> None:
        async with get_async_session_context() as session:
            user_account = await session.get(UserAccount, id)
            if account is not None:
                user_account.account = account
            if email is not None:
                user_account.email = email
            if password is not None:
                user_account.password = password
            if address is not None:
                user_account.address = address                                          
            await session.commit()                              

    @staticmethod
    async def select_all() -> List[UserAccount]:#List:資料型態 #UserAccount:資料表 #select_all():查詢所有資料 #async:非同步函數 #->:回傳值 #List[UserAccount]:回傳值型態 
        async with get_async_session_context() as session:#get_async_session_context() 建立資料庫連線 #session:資料庫連線 
            result = await session.execute(select(UserAccount))#result:資料庫查詢結果 #await:等待資料庫操作完成 #execute:執行資料庫操作 #select(UserAccount):查詢資料表所有資料
            user_accounts = result.scalars().all()#user_accounts:資料表所有資料
            return user_accounts

    @staticmethod
    async def select_user_account(id: int = None, account: str = None, email: str = None) -> List[UserAccount]:
        async with get_async_session_context() as session:
            result = await session.execute(
                select(UserAccount).where((UserAccount.id == id) | (UserAccount.account == account) | (UserAccount.emal == email)) #where:查詢條件 #|:或 #&:且 #==:等於 #!=:不等於 #>:大於 #<:小於 #>=:大於等於 #<=:小於等於 #in:在...之中 #not in:不在...之中 #like:相似
            )
            user_account = result.scalars().first()
            return user_account    