import json
import time

from pymongo import MongoClient

from common.aws_utils import AwsUtils

class MyMongo():
    def call_log_id(self, call_sid: str, start_time: time = None):
        call_sid += 'foo'
        if not start_time:
            start_time = time.time()
        start_time_local = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
        print(f"### called with: {start_time_local}")
        sleep_time = 1
        maximum_wait_seconds = 30
        call_log_id = self.db['callLog'].find_one({'callSid':call_sid})['_id']
        print(f"### found call_log_id: {call_log_id}")
        if call_log_id:
            return call_log_id
        if time.time() > start_time + maximum_wait_seconds:
            print(f"### failing...")
            start_time_local = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
            error_message = f"Started polling for callLogId at: {start_time_local}. Maximum wait time {maximum_wait_seconds} seconds exceeded. CallSID: '{call_sid}'"
            print(error_message)
            return
        time.sleep(sleep_time)
        return call_log_id(call_sid, start_time)

    def __init__(self):
        secrets = json.loads(AwsUtils.get_secret(self, 'revtest/hub-apps'))
        mongo_url = secrets.get('mongodb.uri')
        username = secrets.get('mongodb.username')
        password = secrets.get('mongodb.password')
        mongo_url = mongo_url.replace('mongodb://', f"mongodb://{username}:{password}@")
        mongo_client = MongoClient(host=mongo_url)
        self.db = mongo_client['hub-apps']
        foo = self.call_log_id('60d3b25898c80e002d2c05b0')
        print(f"### foo: {foo}")

def main():
    print("Hello World!")
    MyMongo()

if __name__ == "__main__":
    main()