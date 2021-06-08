        # Create a new SQS queue to receive events from the IvrOutboundCallCompletedEvent topic
        ivr_contact_attempt_completed_event_queue = sqs.Queue(
            self,
            f"-{self.target_environment}-IvrOutboundCallCompletedEvent"
        )

        # Subscribe to the existing IvrOutboundCallCompletedEvent topic arn
        ivr_outbound_call_completed_event_topic_arn = f"arn:aws:sns:us-east-2:304489958799:{self.target_environment}-IvrOutboundCallCompletedEvent"
        ivr_outbound_call_completed_event_topic = sns.Topic.from_topic_arn(
            self,
            f"{self.target_environment}-IvrOutboundCallCompletedEvent",
            ivr_outbound_call_completed_event_topic_arn
        )
        ivr_outbound_call_completed_event_topic.add_subscription(
            sns_subscriptions.SqsSubscription(
                queue=ivr_contact_attempt_completed_event_queue,
                filter_policy = {"revel-target-platform": sns.SubscriptionFilter.string_filter(whitelist=["load-test"])},
                raw_message_delivery = True)
        )

