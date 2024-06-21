from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "dataiot" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "pressure" INT,
    "temperature" INT,
    "timestamp" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
        DROP TABLE IF EXISTS "pressuredata";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "dataiot";"""
