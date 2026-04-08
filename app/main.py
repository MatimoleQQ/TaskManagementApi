from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from . import crud, models, schemas, auth
from .database import engine, get_db

# Tworzymy tabele w bazie
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API", version="0.1.0")

# -------------------------
# USER ENDPOINTS
# -------------------------
@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)


# -------------------------
# AUTH ROUTER
# -------------------------
router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)

    if user is None:
        # email nie istnieje
        if crud.get_user_by_email(db, form_data.username) is None:
            raise HTTPException(status_code=404, detail="User not found")
        # hasło złe
        raise HTTPException(status_code=401, detail="Incorrect password")

    access_token = auth.create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=60)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


app.include_router(router)


# -------------------------
# TASK ENDPOINTS
# -------------------------
@app.post("/tasks/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_task(db, task, user_id=current_user.id)


@app.get("/tasks/", response_model=list[schemas.TaskOut])
def get_tasks(db: Session = Depends(get_db),
              current_user: models.User = Depends(auth.get_current_user)):
    return crud.get_tasks(db, user_id=current_user.id)


@app.delete("/tasks/{task_id}", response_model=schemas.TaskOut)
def delete_task(task_id: int,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):

    task = crud.delete_task(db, task_id=task_id, user_id=current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task