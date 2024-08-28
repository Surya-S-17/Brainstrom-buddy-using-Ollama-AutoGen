from autogen import AssistantAgent, UserProxyAgent

config_list = [
    {
        "model": "mistral",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
    }
]

# Create UserProxyAgent instance
user_proxy_agent = UserProxyAgent(
    name="user",
    human_input_mode="ALWAYS",  # Set to "ALWAYS" to allow user input
    code_execution_config={"use_docker": False},
)

# Create AssistantAgent instance
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="You are a helpful assistant.",
)

project_discription="I'm planning to do a project on slack bot"
assistant_response = user_proxy_agent.initiate_chat(assistant, message=project_discription+"provide a implementation plan for my project")
print(f"{assistant.name}: {assistant_response}")

# Loop to handle conversation
while True:
    user_input = input(f"{user_proxy_agent.name.capitalize()}: ").strip()

    # Exit loop if user enters 'exit'
    if user_input.lower() == 'exit':
        break

    # Continue the conversation by sending user input to AssistantAgent
    assistant_response = user_proxy_agent.continue_chat(user_input)
    print(f"{assistant.name}: {assistant_response}")