from unittest import TestCase
import requests
import json
import uuid
import time
# Create your tests here.


class TestEventStore(TestCase):
    def test_event_store_writes_to_db(self):
        get_endpoint_url = 'http://127.0.0.1:8000/sendClick'
        uniqueID = uuid.uuid4().__str__()
        expected_click_url = 'https://bbc.co.uk/education'+uniqueID
        data = {'clickUrl': expected_click_url}

        request = requests.post(get_endpoint_url, data)

        time.sleep(3)

        arr = json.loads(requests.get('http://127.0.0.1:7000/getData').text)
        print(arr)
        first_element = arr[len(arr)-1]
        actual_click_url = first_element.get('fields').get('click_url')



        self.assertEqual(expected_click_url, actual_click_url)
