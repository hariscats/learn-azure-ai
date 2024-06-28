using Microsoft.SemanticKernel;
using System;
using System.Net.Http;

class Program
{
    static async Task Main(string[] args)
    {
        // Set environment variables for sensitive information
        string deploymentName = Environment.GetEnvironmentVariable("AZURE_DEPLOYMENT_NAME");
        string apiKey = Environment.GetEnvironmentVariable("AZURE_API_KEY");
        string endpoint = Environment.GetEnvironmentVariable("AZURE_ENDPOINT");

        // Ensure all required configurations are present
        if (string.IsNullOrWhiteSpace(deploymentName) ||
            string.IsNullOrWhiteSpace(apiKey) ||
            string.IsNullOrWhiteSpace(endpoint)) 
        {
            Console.WriteLine("Please ensure all environment variables are set correctly.");
            return;
        }

        try
        {
            IKernelBuilder kernelBuilder = Kernel.CreateBuilder();
            kernelBuilder.AddAzureOpenAIChatCompletion(
                deploymentName: deploymentName,
                apiKey: apiKey,
                endpoint: endpoint,
                httpClient: new HttpClient() 
            );

            Kernel kernel = kernelBuilder.Build();

            Console.WriteLine("Chat with the Semantic Kernel. Type 'exit' to quit.");

            while (true)
            {
                Console.Write("You: ");
                string userInput = Console.ReadLine();

                if (userInput?.ToLower() == "exit")
                {
                    break;
                }

                var response = await kernel.InvokePromptAsync(userInput);
                Console.WriteLine($"AI: {response}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}