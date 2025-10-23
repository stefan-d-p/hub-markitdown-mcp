from fastmcp import FastMCP
from markitdown import MarkItDown
from starlette.responses import JSONResponse
from auth import verifier

mcp = FastMCP(
    name="MarkItdown MCP Server",
    version="1.0.0",
    auth=verifier
)

@mcp.tool()
def convert_to_markdown(uri: str) -> str:
    """Convert a resorce described by an http:, https:, or data: URI to markdown"""
    return MarkItDown(
        enable_plugins="false"
    ).convert_uri(uri).markdown

@mcp.custom_route("/health", methods=["GET"])
def health_check(request):
    return JSONResponse({ "status": "healthy", "service": "markitdown-mcp-server" })

app = mcp.http_app(transport="streamable-http", stateless_http="true")

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )