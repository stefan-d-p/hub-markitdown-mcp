# MarkItDown MCP Server

A Model Context Protocol (MCP) server that converts various document formats to Markdown using Microsoft's MarkItDown library.

## Features

- Convert documents from HTTP/HTTPS URLs to Markdown
- Support for data URIs
- JWT authentication with configurable keys
- Health check endpoint
- Docker support for easy deployment

## Supported Formats

This server leverages MarkItDown's capabilities to convert various file formats including:
- PDF documents
- Word documents (.docx)
- PowerPoint presentations (.pptx)
- Excel spreadsheets (.xlsx)
- Images (with OCR)
- Audio files (with transcription)
- And many more formats supported by MarkItDown

## Installation

### Prerequisites

- Python 3.12+
- uv (recommended) or pip

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd markitdown-mcp
```

2. Install dependencies:
```bash
uv sync
```

3. Configure environment variables by copying and editing the development environment file:
```bash
cp .env.development .env
```

4. Edit `.env` with your JWT configuration:
```env
JWT_PUBLIC_KEY="your-jwt-public-key-pem"
JWT_ISSUER="https://your-issuer.com"
JWT_AUDIENCE="your-audience"
```

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t markitdown-mcp .
```

2. Run with Docker Compose:
```bash
docker-compose up -d
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `JWT_PUBLIC_KEY` | JWT public key in PEM format | Built-in default key |
| `JWT_ISSUER` | JWT token issuer | `https://hub.without.systems` |
| `JWT_AUDIENCE` | JWT token audience | `mcp-server` |

## Usage

### As an MCP Server

Add this server to your MCP client configuration:

```json
{
  "mcpServers": {
    "markitdown": {
      "command": "uv",
      "args": ["run", "python", "server.py"],
      "cwd": "/path/to/markitdown-mcp"
    }
  }
}
```

### Available Tools

#### `convert_to_markdown`

Converts a resource from a URI to Markdown format.

**Parameters:**
- `uri` (string): HTTP, HTTPS, or data URI pointing to the document to convert

**Returns:**
- Markdown string representation of the document

**Example:**
```python
# Convert a PDF from a URL
result = convert_to_markdown("https://example.com/document.pdf")
print(result)  # Markdown content
```

### HTTP API

The server also exposes an HTTP API:

#### Health Check
```
GET /health
```

Returns server health status.

#### MCP Tools (via HTTP)
The server supports streamable HTTP transport for MCP protocol communication.

## Development

### Running Locally

```bash
# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Run the server
python server.py
```

The server will start on `http://localhost:8000`.

### Running Tests

```bash
uv run pytest
```

## Authentication

This server uses JWT authentication. Ensure your JWT tokens are signed with the private key corresponding to the configured public key and include the correct issuer and audience claims.

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions, please open an issue on the repository or contact stefan.weber@without.systems.