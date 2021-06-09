import boto3
import json

sqs = boto3.client('sqs')
url = 'https://sqs.us-east-2.amazonaws.com/304489958799/ChrisThompson-gather-billing-event'

print(f"Polling SQS queue url: '{url}'")
sqs = boto3.client('sqs')
filename = 'gather-billing-event.json'
with open(filename, 'w') as outfile:
    print('Polling...')
    messages = sqs.receive_message(QueueUrl=url, MaxNumberOfMessages=10, WaitTimeSeconds=20)
    while 'Messages' in messages: # when the queue is exhausted, the response dict contains no 'Messages' key
        for message in messages['Messages']:  # 'Messages' is a list
            body = json.loads(message['Body'])
            timestamp = body['Timestamp']
            inner_message = json.loads(body['Message'])
            inner_message['awsTimestamp'] = timestamp
            json.dump(inner_message, outfile, indent=4)
            outfile.write('\n')
            sqs.delete_message(QueueUrl=url, ReceiptHandle=message['ReceiptHandle'])
        print('Polling...')
        messages = [] # sqs.receive_message(QueueUrl=url, MaxNumberOfMessages=10, WaitTimeSeconds=20)

print('done')
