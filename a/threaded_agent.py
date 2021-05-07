import concurrent.futures
import threading

import requests


class Agent:
    """
    As simple agent that makes a http request and stores a response.
    """
    def __init__(self, session, url):
        with session.get(url) as response:
            self.response = response


class Orchestrator:
    """
    A simple client orchestrator that can can spawn `N` agents on
    individual threads. Stores the responses in a dictionary.

    """
    _resp_buckets = {
                "Good checkin": 0,
                "Bad request": 0,
                "Server error": 0,
            }
    _thread_local = threading.local()
       
    @property
    def response_buckets(self):
        return self._resp_buckets

    @property
    def total_responses_collected(self):
        return self._resp_buckets["Good checkin"] \
                    + self._resp_buckets["Bad request"] \
                    + self._resp_buckets["Server error"]
   
    def run_clients(self, url, num_clients=10):
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=num_clients) as executor:
            futures = list()
            for t in range(num_clients):
                session = self._get_session()
                futures.append(executor.submit(Agent, session, url))
            
            for future in futures:
                agent = future.result()
                self._log_response(agent.response)
    
    def _get_session(self):
        """Get a thread-safe requests.Session()"""
        if not hasattr(self._thread_local, "session"):
            self._thread_local.session = requests.Session()
        return self._thread_local.session

    def _log_response(self, resp):
        json = resp.json()
        self._resp_buckets[json['Message']] += 1
    

if __name__ == "__main__":
    """
    Create an agent the checks in with a most basic server.
    Store responses into their respective buckets so we can
    introspect the behavior of the system.

    Expand to allow for threading/concurrency
    """
    url = 'http://127.0.0.1:5001/v1/checkin'

    orchestrator = Orchestrator()
    orchestrator.run_clients(url, 1000)

    print(orchestrator.response_buckets)
    print(orchestrator.total_responses_collected)
