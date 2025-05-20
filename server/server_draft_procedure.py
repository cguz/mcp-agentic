from mcp.server.fastmcp import FastMCP

mcp = FastMCP("UC-1 Draft Procedure")

@mcp.tool()
async def get_draft(name: str) -> str:
    """Get draft of a procedure."""
    return "This is a draft procedure for the procedure " + name

if __name__ == "__main__":
    mcp.run(transport="streamable-http")