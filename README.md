# ai-compliance-scanner
AI-powered cloud scanner that flags PII in documents using Amazon Comprehend.
# 🔐 AI-Powered PII Scanner using Amazon Comprehend

This project uses **Amazon Comprehend** to automatically detect sensitive Personally Identifiable Information (PII) in uploaded documents. It showcases a simple but powerful use of serverless AI for real-world compliance and security use cases.

---

## 📌 Overview

- Upload a `.txt` document.
- Script sends the text to **Amazon Comprehend**.
- Comprehend detects entities like names, SSNs, phone numbers, emails, and addresses.
- Detected PII is displayed in an easy-to-understand format.

---

## 📸 Architecture Diagram

![Architecture Diagram](architecture/AI_Comprehend_PII_Diagram.png)

---

## 🎯 Objectives

- Demonstrate a no-code/low-code AI workflow on AWS.
- Show how AI services can assist with GRC (Governance, Risk, and Compliance).
- Provide a testable, functional showcase for recruiters.

---

## 🧪 How to Test

1. Clone or download this repo.
2. Open `scanner/pii_scanner.py`.
3. Ensure your AWS credentials are set up.
4. Run:

```bash
python pii_scanner.py
---

## 🚀 Try It Out

To quickly see how the scanner works:

1. Open the `sample-documents/example_1.txt` file (included in this repo).
2. Imagine this file is uploaded to the system.
3. The AI scanner identifies any PII such as:
   - Names
   - SSNs
   - Phone numbers
   - Addresses
4. Detected PII would be highlighted or logged by the `scanner/pii_scanner.py` script.

Want to run it live? Clone the repo, install the requirements, and run:

```bash
python scanner/pii_scanner.py
```

---
