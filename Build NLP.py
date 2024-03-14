key = "{REPLACE-WITH-YOUR-VALUE}"
endpoint = "{REPLACE-WITH-YOUR-VALUE}"
project_name = "{REPLACE-WITH-YOUR-VALUE}"
deployment_name = "{REPLACE-WITH-YOUR-VALUE}"

import sys
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient


def main():
    # analyze query
    if (len(sys.argv) > 1):
        query = sys.argv[1]
    else:
        query = "Send an email to Carol about the tomorrow's demo"
    
    client = ConversationAnalysisClient(endpoint, AzureKeyCredential(key))

    with client:
        result = client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "en",
                        "text": query
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": project_name,
                    "deploymentName": deployment_name,
                    "verbose": True
                }
            }
        )
    # view result
    print(f"query: {result['result']['query']}")

    if result['result']['prediction']['intents'][0]['confidenceScore'] > 0.8:
        print(f"category: {result['result']['prediction']['intents'][0]['category']}")
        print(f"confidence score: {result['result']['prediction']['intents'][0]['confidenceScore']}\n")
        print("entities:")
        for entity in result['result']['prediction']['entities']:
            print(f"\ncategory: {entity['category']}")
            print(f"text: {entity['text']}")
            print(f"confidence score: {entity['confidenceScore']}")


if __name__ == '__main__':
    main()
