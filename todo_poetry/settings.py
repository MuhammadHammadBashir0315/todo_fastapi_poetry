from sqlmodel import Field,Session,SQLModel,create_engine,select





engine = create_engine(
    "postgresql://hammad.bashir0315:JPtH6Ecbpk0x@ep-tiny-bar-64942038.us-east-2.aws.neon.tech/neondb?sslmode=require", echo=True
)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine )
def get_session():
    with Session(engine) as session:
        yield session