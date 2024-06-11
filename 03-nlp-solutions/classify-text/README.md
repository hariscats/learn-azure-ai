### Instructions

**Custom Text Classification with Azure AI Language**

1. **Provision Azure AI Language Resource:**
   - Sign in to the Azure portal.
   - Search for Azure AI services and create a Language Service resource.
   - Enable the Custom text classification feature.
   - Configure and create the resource with necessary settings.
   - Note the Keys and Endpoint.

2. **Upload Sample Articles:**
   - Download sample articles from [classification-articles](https://aka.ms/classification-articles).
   - Navigate to the storage account in Azure portal.
   - Enable Blob anonymous access.
   - Create a container named `articles` with appropriate access level.
   - Upload the sample articles to this container.

3. **Create Custom Text Classification Project:**
   - Open Azure AI Language Studio.
   - Select your Language resource and start a Custom text classification project.
   - Follow the prompts to connect storage, select project type, and enter basic information.
   - Choose your articles container and label the files for training and testing.

4. **Label Data:**
   - Use Data labeling in Language Studio to assign classes (Classifieds, Sports, News, Entertainment) and datasets (training, testing) to articles.
   - Save labels after labeling.

5. **Train Your Model:**
   - Go to Training jobs and start a new training job named ClassifyArticles.
   - Use manual split for training and testing data.
   - Start training and wait for it to complete.

6. **Evaluate Your Model:**
   - Check Model performance to view scoring and metrics.
   - Use the Test set details tab to identify and analyze incorrect predictions.

7. **Deploy Your Model:**
   - Go to Deploying model and add a deployment named `articles`.
   - Deploy the model and note the project and deployment names.

8. **Develop an App in Visual Studio Code:**
   - Clone the repository [mslearn-ai-language](https://github.com/MicrosoftLearning/mslearn-ai-language).
   - Open the cloned repo in Visual Studio Code.
   - Follow prompts to install additional files for C# code projects.

9. **Set Environment Variables:**

**For PowerShell:**
```powershell
$env:AZURE_AI_ENDPOINT = "<your-endpoint>"
$env:AZURE_AI_KEY = "<your-key>"
```

**For Bash:**
```bash
export AZURE_AI_ENDPOINT="<your-endpoint>"
export AZURE_AI_KEY="<your-key>"
```