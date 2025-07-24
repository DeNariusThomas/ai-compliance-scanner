import boto3
import os

def detect_pii(text):
    client = boto3.client('comprehend')
    response = client.detect_pii_entities(
        Text=text,
        LanguageCode='en'
    )
    return response['Entities']

if __name__ == "__main__":
    with open("sample-documents/example_1.txt", "r") as file:
        text = file.read()
        pii_entities = detect_pii(text)
        if pii_entities:
            print("🔒 PII Detected:")
            for entity in pii_entities:
                print(f"- Type: {entity['Type']}, Score: {entity['Score']:.2f}")
        else:
            print("✅ No PII detected.")
