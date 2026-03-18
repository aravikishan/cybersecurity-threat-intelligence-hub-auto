
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String)

class ThreatIndicator(Base):
    __tablename__ = "threat_indicators"
    indicator_id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    description = Column(String)
    severity = Column(String)

class IncidentReport(Base):
    __tablename__ = "incident_reports"
    incident_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    reported_by = Column(String)

# Pydantic models
class UserBase(BaseModel):
    username: str
    email: str
    role: str

class ThreatIndicatorBase(BaseModel):
    type: str
    description: str
    severity: str

class IncidentReportBase(BaseModel):
    title: str
    description: str
    status: str
    reported_by: str

# Create tables
Base.metadata.create_all(bind=engine)

# Seed data
def seed_data():
    db = SessionLocal()
    if not db.query(User).first():
        db.add_all([
            User(username="admin", email="admin@example.com", role="admin"),
            User(username="user1", email="user1@example.com", role="user")
        ])
    if not db.query(ThreatIndicator).first():
        db.add_all([
            ThreatIndicator(type="Malware", description="Malware detected", severity="High"),
            ThreatIndicator(type="Phishing", description="Phishing attempt", severity="Medium")
        ])
    if not db.query(IncidentReport).first():
        db.add_all([
            IncidentReport(title="Unauthorized Access", description="Unauthorized access detected", status="Open", reported_by="admin"),
            IncidentReport(title="Data Breach", description="Sensitive data exposed", status="Closed", reported_by="user1")
        ])
    db.commit()
    db.close()

seed_data()

# FastAPI app
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_dashboard():
    with open("templates/index.html") as f:
        return f.read()

@app.get("/threats", response_class=HTMLResponse)
async def read_threats():
    with open("templates/threats.html") as f:
        return f.read()

@app.get("/incidents", response_class=HTMLResponse)
async def read_incidents():
    with open("templates/incidents.html") as f:
        return f.read()

@app.get("/profile", response_class=HTMLResponse)
async def read_profile():
    with open("templates/profile.html") as f:
        return f.read()

@app.get("/admin", response_class=HTMLResponse)
async def read_admin():
    with open("templates/admin.html") as f:
        return f.read()

@app.get("/api/threat-indicators", response_model=List[ThreatIndicatorBase])
async def get_threat_indicators(db: Session = Depends(get_db)):
    return db.query(ThreatIndicator).all()

@app.post("/api/incidents", response_model=IncidentReportBase)
async def create_incident_report(incident: IncidentReportBase, db: Session = Depends(get_db)):
    db_incident = IncidentReport(**incident.dict())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

@app.get("/api/incidents", response_model=List[IncidentReportBase])
async def get_incident_reports(db: Session = Depends(get_db)):
    return db.query(IncidentReport).all()

@app.get("/api/users", response_model=List[UserBase])
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.put("/api/users/{user_id}", response_model=UserBase)
async def update_user(user_id: int, user: UserBase, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user
