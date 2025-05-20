from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Retrival")

@mcp.tool()
def ved(query: str) -> int:
    """Get information from the Vector Database"""
    return "This is the information retrieved for the query: " + query


@mcp.tool()
def graph(query: str) -> int:
    """Get information from the Knowledge Graph"""
    return "This is the information retrieved for the query: " + query

@mcp.tool()
def external_tools(query: str) -> int:
    """Get information from external tools"""
    return "This is the information retrieved for the query: " + query

if __name__ == "__main__":
    print("Starting MCP server for knowledge retrieval...")
    mcp.run(transport="stdio")