from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SentinelIQ</title>
    </head>
    <body style="background:#0d1117;color:#58a6ff;font-family:Arial;text-align:center;padding-top:100px;">
        <h1>SentinelIQ</h1>
        <h2>Backend is Working</h2>
    </body>
    </html>
    """