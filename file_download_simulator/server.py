
import asyncio
import time
import requests
import aiohttp
import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


from starlette.concurrency import run_in_threadpool

@app.get("/sync-download")
async def sync_download():
    async def file_generator():
        total_files = 5
        base_url = "https://www.gutenberg.org/files/1342/1342-0.txt"
        for i in range(1, total_files + 1):
            # Simulate a real download using requests in a threadpool
            response = await run_in_threadpool(requests.get, base_url)
            response.raise_for_status()
            content_snippet = response.text[:50]  # Get first 50 chars
            cleaned_content_snippet = content_snippet.replace('\n', ' ')
            payload = {"file": i, "total": total_files, "status": "descargado", "content": cleaned_content_snippet}
            yield f"data: {json.dumps(payload)}\n\n"
        yield f"data: {json.dumps({'status': 'completo'})}\n\n"

    return StreamingResponse(file_generator(), media_type="text/event-stream")


@app.get("/async-download")
async def async_download():
    async def file_generator():
        total_files = 5
        
        async def download_file(i):
            base_url = "https://www.gutenberg.org/files/1342/1342-0.txt"
            async with aiohttp.ClientSession() as session:
                async with session.get(base_url) as response:
                    response.raise_for_status()
                    content_snippet = (await response.text())[:50]  # Get first 50 chars
                    cleaned_content_snippet = content_snippet.replace('\n', ' ')
                    payload = {"file": i, "total": total_files, "status": "descargado", "content": cleaned_content_snippet}
                    return f"data: {json.dumps(payload)}\n\n"

        tasks = [download_file(i) for i in range(1, total_files + 1)]
        
        for future in asyncio.as_completed(tasks):
            result = await future
            yield result
            
        yield f"data: {json.dumps({'status': 'completo'})}\n\n"

    return StreamingResponse(file_generator(), media_type="text/event-stream")

