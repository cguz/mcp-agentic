from mcp.server.fastmcp import FastMCP

MCP_SERVER_KNOWLEDGE_RETRIEVAL =  {
            # Ensure your start your weather server on port 8000
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }

mcp = FastMCP("Retrival")

@mcp.tool()
async def ved(query: str) -> int:
    """Get information from the Vector Database"""
    return "This is the information retrieved for the query: " + query

@mcp.tool()
async def graph(query: str) -> int:
    """Get information from the Knowledge Graph"""
    return "This is the information retrieved for the query: " + query

@mcp.tool()
async def external_tools(query: str) -> int:
    """Get information from external tools"""
    return "This is the information retrieved for the query: " + query

if __name__ == "__main__":
    mcp.run(transport="streamable-http")