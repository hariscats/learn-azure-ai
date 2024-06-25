## Use Prebuilt Document Intelligence Models

### Overview
Set up an Azure AI Document Intelligence resource and submit forms for analysis using Python.

### Steps

#### 1. Create Azure AI Document Intelligence Resource
1. Open [Azure Portal](https://portal.azure.com) and sign in.
2. Search for "Document Intelligence" and select **Create**.
3. Configure the resource:
   - **Subscription**: Your Azure subscription.
   - **Resource Group**: Create or select `DocIntelligenceResources`.
   - **Region**: Select a nearby region.
   - **Name**: Enter a unique name.
   - **Pricing tier**: Select Free F0 (or Standard S0 if Free is unavailable).
4. Click **Review + create**, then **Create**.
5. After deployment, select **Go to resource** and keep this page open.


#### 2. Configure Your Application
2. Install the required package:
   ```sh
   pip install azure-ai-formrecognizer==3.3.0
   ```
2. Run Python application:
   ```sh
   python main.py
   ```