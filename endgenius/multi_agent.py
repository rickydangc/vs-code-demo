def create_multi_agent(agent1, agent2, multi_agent_message=None):
    # Check if the multi_agent_message is provided and not already in the content of the agents
    # This multi_agent_message is used to define the guidance for how should multi agent work together
    if multi_agent_message and multi_agent_message not in agent1['content'] and multi_agent_message not in agent2['content']:
        # Combine the content of the two agents and add the multi_agent_message at the front
        combined_content = multi_agent_message + '; ' + agent1['content'] + '; ' + agent2['content']
    else:
        # Combine the content of the two agents without adding the multi_agent_message
        combined_content = agent1['content'] + '; ' + agent2['content']

    # Create the new multi_agent with the combined content
    multi_agent = {
        "role": "system",
        "content": combined_content
    }

    return multi_agent