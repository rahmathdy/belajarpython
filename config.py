# Koneksi dari Flask ke Postgres

class Config:
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://usrdemo:abc123abc456@localhost:5432/resepinix"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
