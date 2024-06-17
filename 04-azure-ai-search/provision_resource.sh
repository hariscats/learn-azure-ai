#!/bin/bash

# Load environment variables from .env file
source .env

# Set variables
RESOURCE_GROUP=$1
SEARCH_SERVICE_NAME=$2
AI_SERVICE_NAME=$3
STORAGE_ACCOUNT_NAME=$4
LOCATION=$5

# Check if all arguments are provided
if [ $# -ne 5 ]; then
    echo "Usage: $0 <resource-group> <search-service-name> <ai-service-name> <storage-account-name> <location>"
    exit 1
fi

# Create resource group
echo "Creating resource group..."
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create Azure AI Search resource
echo "Creating Azure AI Search resource..."
az search service create --name $SEARCH_SERVICE_NAME --resource-group $RESOURCE_GROUP --sku Basic --location $LOCATION

# Create Azure AI Services resource
echo "Creating Azure AI Services resource..."
az cognitiveservices account create --name $AI_SERVICE_NAME --resource-group $RESOURCE_GROUP --kind CognitiveServices --sku S0 --location $LOCATION --yes

# Create Storage account
echo "Creating Storage account..."
az storage account create --name $STORAGE_ACCOUNT_NAME --resource-group $RESOURCE_GROUP --location $LOCATION --sku Standard_LRS --kind StorageV2 --allow-blob-public-access true

# Get storage account keys
echo "Getting Storage account keys..."
STORAGE_KEY=$(az storage account keys list --resource-group $RESOURCE_GROUP --account-name $STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv)

# Display information
echo "Resource group: $RESOURCE_GROUP"
echo "Azure AI Search service: $SEARCH_SERVICE_NAME"
echo "Azure AI Services: $AI_SERVICE_NAME"
echo "Storage account: $STORAGE_ACCOUNT_NAME"
echo "Storage account key: $STORAGE_KEY"
