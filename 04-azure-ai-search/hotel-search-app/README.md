# Azure AI Search and Flask App

This directory contains a script to provision the necessary Azure resources for an Azure AI Search solution, as well as a Flask app that interacts with these resources to perform search queries and display results.

## Prerequisites

- Azure CLI installed
- Azure subscription
- Bash shell
- Python 3.x installed
- `pip` package installer

## Provisioning Azure Resources

### Usage

1. Run the script with the required parameters:
    ```bash
    ./provision_resources.sh <resource-group> <search-service-name> <ai-service-name> <storage-account-name> <location>
    ```

    Example:
    ```bash
    ./provision_resources.sh margies-travel-rg margies-search-service margies-ai-service margiesstorage eastus
    ```

### Parameters

- `<resource-group>`: The name of the resource group to create or use.
- `<search-service-name>`: A unique name for the Azure AI Search service.
- `<ai-service-name>`: A unique name for the Azure AI Services resource.
- `<storage-account-name>`: A unique name for the Storage account.
- `<location>`: The Azure region where the resources will be created (e.g., eastus).

### Notes

- Ensure that the Azure AI Search and Azure AI Services resources are created in the same location.
- The script also outputs the storage account key, which is needed for accessing the storage account.

### Post-Provisioning Steps

1. Navigate to the Azure portal to verify the creation of resources.
2. Use the Azure portal to configure data sources, indexes, indexers, and skillsets for the Azure AI Search service.
3. Store documents in the created Storage account for indexing by the Azure AI Search service.

## Flask Application

### Overview

The Flask application provides a web interface to interact with the Azure AI Search service. Users can perform search queries and view results through the web interface.

### Configuration

1. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the root directory of the project with the following environment variables:
    ```env
    SEARCH_SERVICE_ENDPOINT=<your-search-service-endpoint>
    SEARCH_SERVICE_QUERY_KEY=<your-search-service-query-key>
    SEARCH_INDEX_NAME=<your-search-index-name>
    ```

3. Ensure that the `.env` file contains the correct values for your Azure AI Search service.

### Running the Application

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://127.0.0.1:5000` to access the home page.

### Application Structure

- **app.py**: The main application file that defines routes and handles search queries.
- **templates/**: Contains HTML templates for rendering web pages.
  - `default.html`: The home page template.
  - `search.html`: The search results page template.
  - `error.html`: The error page template.
