# import boto3
# import csv
# import json
# import time

# sqs = boto3.client('sqs')
# url = 'https://sqs.us-east-2.amazonaws.com/304489958799/ChrisThompson-gather-billing-event'

# print(f"Polling SQS queue url: '{url}'")
# sqs = boto3.client('sqs')
# ten_seconds = 10
# timeout = time.time() + ten_seconds
# filename = 'gather-billing-event.csv'
# fieldnames = ['callId', 'gatherCount', 'id', 'createdAtUtc', 'tenantId', 'programId', 'correlationId', 'causationId', 'memberSystemInformation', 'messageContextDataMap', 'timestamp']
# with open(filename, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(fieldnames)
# with open(filename, 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames)
#     print('Polling...')
#     messages = sqs.receive_message(QueueUrl=url, MaxNumberOfMessages=10, WaitTimeSeconds=20)
#     while 'Messages' in messages: # when the queue is exhausted, the response dict contains no 'Messages' key
#         for message in messages['Messages']:  # 'Messages' is a list
#             body = json.loads(message['Body'])
#             timestamp = body['Timestamp']
#             inner_message = json.loads(body['Message'])
#             inner_message['timestamp'] = timestamp
#             writer.writerow(inner_message)
#             timeout = time.time() + ten_seconds
#             sqs.delete_message(QueueUrl=url, ReceiptHandle=message['ReceiptHandle'])
#         print('Polling...')
#         messages = sqs.receive_message(QueueUrl=url, MaxNumberOfMessages=10, WaitTimeSeconds=20)

# print('done')
