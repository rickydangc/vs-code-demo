#Some helpful functions to manage the payload that are going to be used for sending requests:
def change_payload(payload, model=None, temperature=None, task=None, messages=None, ):
    if model is not None:
        payload["model"] = model
    if task is not None:
        payload["task"] = task
    if messages is not None:
        payload["model-params"]["messages"] = messages
    if temperature is not None:
        payload["model-params"]["temperature"] = temperature
    return payload

#Used for change user content
def change_message_content_for_user(payload, new_content):
    for message in payload["model-params"]["messages"]:
        if message["role"] == "user":
            message["content"] = new_content

def add_agent(payload,agent):
    payload["model-params"]["messages"].insert(0, agent)

def generate_payload_with_agent(payload,new_content,agent):
    change_message_content_for_user(payload,new_content)
    add_agent(payload,agent)