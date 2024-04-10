# You can use it for testing different model, request or agent.
import make_llm_request
import agent
import multi_agent
R2_request = "Use R2 framework to write a testing script for testing login on IOS, explain your script"
testcafe_request = """
                Use testcafe framework to write a testing script, which can test the following steps:
                    /**
                    * Steps
                    * =====
                    * Home page load
                    * sign in
                    * Clear the cart
                    * add 2 unscheduled pickup items to cart and increase quantity to two
                    * cart validations
                    * Checkout page validations
                    */
                """,
multi_agent_request = "can explain me about walmart"
multi_agent_message ="You are a multi agent Generate the response as combined response and tell which response is from which agent"
#multi_agent = multi_agent.create_multi_agent(agent.multi_agent1,agent.multi_agent3,multi_agent_message)
#make_llm_request.make_request(multi_agent_request, multi_agent, "gpt-4-turbo")
make_llm_request.make_request(testcafe_request, agent.testcafe_agent, "gpt-4-turbo")