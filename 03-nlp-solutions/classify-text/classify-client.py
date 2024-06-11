# import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Create client using endpoint and key
credential = AzureKeyCredential(ai_key)
ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

# Get Classifications
operation = ai_client.begin_single_label_classify(
    batchedDocuments,
    project_name=project_name,
    deployment_name=deployment_name
)

document_results = operation.result()

for doc, classification_result in zip(files, document_results):
    if classification_result.kind == "CustomDocumentClassification":
        classification = classification_result.classifications[0]
        print("{} was classified as '{}' with confidence score {}.".format(
            doc, classification.category, classification.confidence_score)
        )
    elif classification_result.is_error is True:
        print("{} has an error with code '{}' and message '{}'".format(
            doc, classification_result.error.code, classification_result.error.message)
        )

