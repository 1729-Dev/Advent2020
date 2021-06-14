import boto3
import json

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-2.amazonaws.com/304489958799/ChrisThompson-gather-billing-event'

print(f"Polling SQS queue url: '{queue_url}'")
sqs = boto3.client('sqs')
messages_data = []
messages = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10, WaitTimeSeconds=20)
while 'Messages' in messages: # when the queue is exhausted, the response dict contains no 'Messages' key
    print(f"Found {len(messages_data)} messages so far")
    for message in messages['Messages']:  # 'Messages' is a list
        body = json.loads(message['Body'])
        timestamp = body['Timestamp']
        inner_message = json.loads(body['Message'])
        inner_message['awsTimestamp'] = timestamp
        messages_data.append(inner_message)
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])
    messages = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10, WaitTimeSeconds=20)
filename = 'foo.json'
with open(filename, 'w') as outfile:
    json.dump(messages_data, outfile, ensure_ascii=False, indent=4)
print(f"Finished polling.  Saved: {len(messages_data)} events")

print('done')
