import fastmcp
import json 
mcp=fastmcp.FastMCP("calculator")
@mcp.tool
def add(a: int, b: int) -> int:
    return a + b
@mcp.tool
def subtract(a: int, b: int) -> int:
    return a - b

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
