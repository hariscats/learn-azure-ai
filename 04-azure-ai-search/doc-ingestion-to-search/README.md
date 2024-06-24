### README

## Add to an Index Using the Push API

### Overview
Learn to create an Azure AI Search index and upload documents using C# code. You'll clone an existing solution, determine the optimal batch size for uploads, and use threading for efficient data ingestion.

### Steps

#### 1. Set Up Azure Resources
1. **Deploy Resources**: Use the ARM template to create necessary resources.
2. **Resource Group**: Name it `cog-search-language-exe` and select a supported region.
3. **Resource Prefix**: Enter a unique prefix, e.g., `acs118245`.
4. **Review + Create**: Deploy the resources and navigate to the resource group.

#### 2. Copy Azure AI Search Service Information
1. **Select Search Service**: Note the name of the search service.
2. **Keys**: Copy the Primary admin key.

#### 3. Download Example Code
1. **Open Azure Cloud Shell**: 
   - Open code editor: `code ./optimize-data-indexing/v11`
2. **Edit Configuration**:
   - In `appsettings.json`, update with your search service name and key:
     ```json
     {
       "SearchServiceUri": "https://acs118245-search-service.search.windows.net",
       "SearchServiceAdminApiKey": "YOUR_SEARCH_SERVICE_KEY",
       "SearchIndexName": "optimize-indexing"
     }
     ```
   - Update `OptimizeDataIndexing.csproj`:
     ```xml
     <TargetFramework>net7.0</TargetFramework>
     ```
3. **Run Application**:
   - Change directory: `cd ./optimize-data-indexing/v11/OptimizeDataIndexing`
   - Run the app: `dotnet run`

#### 4. Implement Threading and Backoff Strategy
1. **Edit `Program.cs`**:
   - Comment out lines 38 and 39 if not already:
     ```csharp
     //Console.WriteLine("{0}", "Finding optimal batch size...\n");
     //await TestBatchSizesAsync(searchClient, numTries: 3);
     ```
   - Uncomment lines 41 to 49:
     ```csharp
     long numDocuments = 100000;
     DataGenerator dg = new DataGenerator();
     List<Hotel> hotels = dg.GetHotels(numDocuments, "large");

     Console.WriteLine("{0}", "Uploading using exponential backoff...\n");
     await ExponentialBackoff.IndexDataAsync(searchClient, hotels, 1000, 8);

     Console.WriteLine("{0}", "Validating all data was indexed...\n");
     await ValidateIndexAsync(indexClient, indexName, numDocuments);
     ```
2. **Save Changes**: Press `CTRL + S`.
3. **Run Application**: 
   - In terminal: `dotnet run`

### Validation
- Ensure documents are added by checking the search index in the Azure portal.

### Cleanup
1. **Delete Resources**:
   - In the Azure portal, go to Resource groups.
   - Select the resource group and delete it.
   - Confirm deletion.


For further exploration, check the code in `TestBatchSizesAsync`, `IndexDataAsync`, and `ExponentialBackoffAsync` procedures.