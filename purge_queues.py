# import boto3

# sqs = boto3.client('sqs')
# urls = [
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestTwilioQueueCallCmd61FD996-MWR17CT4UUDP",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestIvrContactAttemptComplete-VM2E8YKE5SAD",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestIvrOutboundCallCompletedE-1683P6DG3C7R8",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestCallRecordingDurationBill-FDRE0C7B0BHU",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestRecordingUploadedEvent969-LMWFJ4207CXK",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestAnsweringMachineDetection-1HSXC9ZFNR7ZB",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestCallDurationBillingEvent6-DPAP1UMF8TZH",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestGatherBillingEvent97D9B20-2QHJ5XUD3KL6",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestBackupTwilioQueueCallCmdE-1SN1QD0DK7QUR",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestBackupIvrContactAttemptCo-12QKPN7Q09ZCN",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestBackupIvrOutboundCallComp-7YK2EEK8YNUS",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestBackupCallRecordingDurati-VTBSGR93ZF3E",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestBackupRecordingUploadedEv-1T4S1KRRIZBX2",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestBackupAnsweringMachineDet-1G9DNLZ2HXYSM",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestBackupCallDurationBilling-1TT0OI174K7S6",
#     "https://sqs.us-east-2.amazonaws.com/304489958799/channel-service-load-tests-revtes-revtestBackupGatherBillingEvent0-R65US5ENTNZO"
# ]

# for url in urls:
#     print(f"purging: {url}")
#     response = sqs.purge_queue(
#         QueueUrl=url
#     )
#     print(response)

# print('done')
