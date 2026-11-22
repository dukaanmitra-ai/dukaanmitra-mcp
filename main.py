import uvicorn
from mcp_server import mcp_router
from fastapi import FastAPI

app = FastAPI(title='DukaanMitra MCP Gateway', version='2.0.0', description='Model Context Protocol (MCP) server for Indian SMBs & Kirana stores.')
app.include_router(mcp_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
