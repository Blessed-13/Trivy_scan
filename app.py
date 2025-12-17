# TEST 1: Hardcoded Secret (Trivy should catch this)
# In a real app, use environment variables or AWS Secrets Manager!
import os
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID") # Secure way

def start_server():
    print("Starting the Cloud/DevOps Test Server...")
    # Mock logic for your Lambda function
    print(f"Connecting to AWS with key: {AWS_ACCESS_KEY[:4]}****")

if __name__ == "__main__":
    start_server()