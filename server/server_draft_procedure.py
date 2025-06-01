from mcp.server.fastmcp import FastMCP

MCP_TOOL_DRAFT_PROCEDURE = {
            "command": "python",
            # Replace with absolute path to your math_server.py file
            "args": ["./server/server_draft_procedure.py"],
            "transport": "stdio",
        }

mcp = FastMCP("UC-1 Draft Procedure")

@mcp.tool()
def get_draft(name: str) -> str:
    """Get draft of a procedure."""
    return "This is a draft procedure for the procedure " + name

if __name__ == "__main__":
    print("Starting MCP server for draft procedure...")
    mcp.run(transport="stdio")