from pydantic import BaseModel, EmailStr

# -------------------------
# USER SCHEMAS
# -------------------------

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


# -------------------------
# TASK SCHEMAS
# -------------------------

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    completed: bool
    owner_id: int

    class Config:
        orm_mode = True