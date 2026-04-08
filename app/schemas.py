from pydantic import BaseModel, EmailStr,Field

# -------------------------
# USER SCHEMAS
# -------------------------

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=72, description="Password must be 8-72 characters long")

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
    title: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)

class TaskOut(TaskBase):
    id: int
    completed: bool
    owner_id: int

    class Config:
        orm_mode = True