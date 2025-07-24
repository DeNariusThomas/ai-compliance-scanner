import boto3
import json

def detect_pii_entities(text):
    comprehend = boto3.client('comprehend')
    
    response = comprehend.detect_pii_entities(
        Text=text,
        LanguageCode='en'
    )
    
    return response['Entities']

def scan_document(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        
    entities = detect_pii_entities(content)
    
    results = []
    for entity in entities:
        results.append({
            "Type": entity["Type"],
            "Score": round(entity["Score"] * 100, 2)
        })
    
    return results

if __name__ == "__main__":
    file_to_scan = "sample.txt"  # Replace with your test file path
    print(json.dumps(scan_document(file_to_scan), indent=2))
