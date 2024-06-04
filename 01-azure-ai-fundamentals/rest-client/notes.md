### Notes

#### Loading Configuration
- **Purpose**: Load AI service endpoint and key from a `.env` file.
- **Key Functions**: `load_dotenv()`, `os.getenv()`.
- **Error Handling**: Raises `ValueError` if required environment variables are missing.

#### Detecting Language
- **Purpose**: Detect the language of provided text using Azure AI services.
- **Steps**:
  - Construct JSON request body.
  - Make HTTP POST request to Azure Text Analytics language API.
  - Include AI service subscription key in headers.
  - Handle response: Check status, parse, and display detected language or errors.
- **Error Handling**: Print exceptions during the process.

#### Main Function
- **Purpose**: Entry point, handles user input and initiates language detection.
- **Steps**:
  - Load configuration.
  - Continuous user prompt for text input.
  - Handle single and batch processing of texts.
  - Call `get_language()` for each text.
- **Error Handling**: Print setup exceptions.

#### General Notes
- **Environment Variables**: Store configuration details in a `.env` file.
- **HTTP Requests**: Use `http.client` for secure HTTP requests.
- **JSON Handling**: Construct and parse JSON objects.
- **Error Handling**: Manage and display errors at various stages.
- **User Interaction**: Interactive mode for single and batch text processing.
