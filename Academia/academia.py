from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./crossfit_competition.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de dados
class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    skill_level = Column(String)

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Criação da aplicação FastAPI
app = FastAPI()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um novo participante
@app.post("/participants/")
async def create_participant(name: str, age: int, skill_level: str, db: Session = Depends(get_db)):
    participant = Participant(name=name, age=age, skill_level=skill_level)
    db.add(participant)
    db.commit()
    db.refresh(participant)
    return participant

# Rota para listar todos os participantes
@app.get("/participants/")
async def read_participants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    participants = db.query(Participant).offset(skip).limit(limit).all()
    return participants

# Rota principal para testar se a API está funcionando
@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Competição de Crossfit!"}
