from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# TODO: Configure CORS
# See `CORSMiddleware`.

# Mock data
PROGRAMMING_LANGUAGES = [
    "JavaScript", "Python", "Java", "C++", "C#", "Ruby", "Go", "Rust",
    "TypeScript", "Swift", "Kotlin", "PHP", "Scala", "Perl", "Haskell"
]

@app.get("/")
async def root():
    return {"message": "Search API is running"}

@app.get("/api/search")
async def search(q: str = ""):
    # TODO: Implement search logic here
    # - Add 500ms delay
    # - Filter PROGRAMMING_LANGUAGES by query (case-insensitive)
    # - Return matching results

    pass  # Replace with your implementation


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
