import requests
import os
import generate_headers
import change_payload
import time
import agent
# Please fill in these details from akeyless
consumer_id = "92795d46-a2fc-4758-b6b3-92e34d8f2b46"
key_version = 2
pvt_key_base64 = "LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2UUlCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktjd2dnU2pBZ0VBQW9JQkFRQ2ttbmtnS2xPMFhhSUgKUHB3T0U4TWF5ZkNGaEk0azRZWXNUUzFhb2VzbU1PQ21KVVZjdU5pbVpDM1hQZ0xwMUVCSFNuNkY1Ulp1aU9NbwppL044Wjdrc1BVWC9tZk02Wk5BQVJaRXViOGY2K2NpYk9GekV3TkM3WFU4WUNVU2t4V0g5WThGQmlaUDNaSjk5CjJQS1U3dzNrSEtQcEdWclpPRmgrU0FyTlY2OGpsNjNzTXljK0o3NHA3VDhKWGhkYjMwUmRha1hWdG5paERDMy8KNE1BUmZWN0d1aXlocEJ3eE9qdXpJK01rQ2w2b0lLbS8zSHlXWmJpQTBxZEM2dnMxazgzUFoyT1d0VjNHRUVCVwowWVNrSGUyekhYcTRzL1JpcnpkT0VuTmUwMGpiT0pMVWNQYW0rMnQwOUlLUlVyWnpGK1N6Z0kyelpsdnVTSVo4ClZmZGJLbWQ5QWdNQkFBRUNnZ0VBZEdzTTRFTVBrTEhvdDFjQTZMUHhlakQ1ZkhXVVUyRnVsRWJCblNpSU9DcTUKdU1rRGxlRG0ya2hnWTZ2b1E1bHJIUUVERzVBN25WSVQxOG1rSElqLzN0bzNkK0JhdHlJMk92cjVBKzdyY2diWQphM0Fock1ieTJwSFVMeHZmQU9yWnMyMnFjYi9zZHowajBNNXdSQVlQdlJiRWwwam5pRnJodSs4WU5NT2ZpM3ZKCldrNnJyNlBWSldCZWl1SW1SdDcrT2VZSnh3eG9LbW0veG14NXZZUFViUnZESURmMnlMV1ozYkpaUTRDT2NjWXMKdWR6STNwWTVaV1lCTmZvcjUyd0FlNTNRbEZQS2RSbS9vM3VUY1ZEUlFvWDdaUmxNck9IQlcwRzdQWWJ1Y1diRAp2dWE4T0s4ellaU1dpZ2dPMjlFeXNzRURGWmpGRlhEaSttYkhFcHZTQVFLQmdRRFZ3emxqT0hROG9NWlRZT0FUCms5RTJaYk1LbHdGNG1nZ3dmTUQ5YWwzQjlJS0V0K0t4RVRxMFBva3kxa0d3dVlRK05DVXJGZEE2dlV1NDdCZ2sKOGppZGhwU2o0VWFiZGpoQVh4WnpKbVRhQVVOcXhPWnA4cnZXZlZuZ1NkT01jbE4yNkZCYkptQ1h2aDJ0NTROUworOTF3T1hhWWlTeUFhSjJsamdCdzRWQnlhUUtCZ1FERklKL3prcnp2VTA1UGloY1BmQWVwK2FMaSsyemxrV05lCjVGbEpXNVUzL1NteFRWOWhacCtpNjJRS0RYeVZua0o0Y25xWVQxNU9WYkNhbHRPMTB0SXMrUWw0SHBESmdrYzYKWk0xcEZJcll2RDA0emlIcjlleVZhUXlUY0lrVXV5TFpjRnIwN3VtVmY5U3FRVERsbS8waTVGTUJVcmliQmg3Ygp2a3Y1TnBhQjlRS0JnUUNWSzhWU2JrVC9RaHJrZUlnbVlWTHdLUXhHYVphSE9NWmFQOVRWZzNLbU5TRVh5Tk1UClNiaXpxNmhHcDZueno2SnZYaWhKNXRFSERLNVkvN2pobjM3T3Z1bmZhd2ZBMlVEcit1OUpzQk5VNXVqTEMxalgKdXFKR1RmZDRRMHl6aDl5aTcvK1RmRGFQN2dYOEk4RkxHYVF2K29tK2JJdDNtSW5hekR1V2lrVi9jUUtCZ0U4eAp5VERZdmRERVBnelVaR2xUSWQwV3JtclVLYTZjMXpnek11KzJ2RjhPOVNZRytJK3Y0K2hXK3d6UzJEOWZva0t6CmN5OG5pN0thMkdWeXZNRXFYa2UxRVNuUjFjY3U4S0MwQ0pYenE4aGc3NU9YdEtjUVdLaTUyRlNQZkhMNHI0cDkKaWYwbTBtNitPVmpnOGR6ODZ4aU9kQTV2QmowNW0wSWExSGpkaGwvVkFvR0FaZDZBblF5ZzJ3QWdRQm9Dd1VNQQpOTTVwb0t2cldBcU5RYmY0aFNvYS9CYXhJUWdoSDRnL1Nwdk5lQ01ib3lCa1hGbVpERDZEQWlML1FPSVdaUndiCmh2dHRJcGFzSUU5RDRub0RKVGMxWWpmWUxyaVhKb2JjdUpBZmdkTWJ5QzNHcHFxVW5BZXJKZTdKbGp5L1FERlcKb1hqYnY0alVDVS9MZnd5NGZuTUJqajg9Ci0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0K"
WMT_CA_PATH = "ca-bundle.crt"  # Check comments on how to get this file
# If you still get SSL error after setting this - try setting REQUESTS_CA_BUNDLE env variable.
os.environ['SSL_CERT_FILE'] = WMT_CA_PATH
os.environ['REQUESTS_CA_BUNDLE'] = WMT_CA_PATH
headers = generate_headers.get_headers(consumer_id, key_version, pvt_key_base64)
def make_request(request, agent, model=None,temperature=None):
    url = "https://wmtllmgateway.stage.walmart.com/wmtllmgateway/v1/openai"
    payload = {
        "model": "gpt-4",
        "task": "chat/completions",
        "model-params": {
            "messages": [
                {
                    "role": "user",
                    "content": "Tell me something interesting about space travel"
                }
            ],
            "temperature": 0.7
        }
    }
    change_payload.change_payload(model,temperature)
    change_payload.generate_payload_with_agent(payload,request,agent)
    print(payload)
    start_time = time.time()
    response = requests.request("POST", url, headers=headers, json=payload)
    end_time = time.time()
    response_time = end_time - start_time
    print(f"The response time is: {response_time:.2f}s")# It can be used to compare model speed
    print(response.json()["choices"][0]["message"]["content"])


