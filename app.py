#!/usr/bin/env python3
from time import time
import asyncio

import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse

from piccolo_conf import MyEntity

app = Starlette(debug=True)

async def add_list(prefix):
    async with MyEntity._meta.db.transaction():
        for i in range(100):
            name = f"{prefix}-{i}-{time():.9f}"
            await MyEntity.objects().get_or_create(MyEntity.name == name)
            await asyncio.sleep(0.05)

@app.route('/add-list/{prefix:str}')
async def r_add_list(request):
    prefix = request.path_params['prefix']
    try:
        await add_list(prefix)
        return JSONResponse(f"{prefix} -> done")
    except Exception as e:
        return JSONResponse(f"{prefix} -> {e}")

if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1', port=64215, reload=True, debug=True)
