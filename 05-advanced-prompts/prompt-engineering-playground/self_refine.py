from azure_client import get_azure_openai_client, create_chat_completion

client, deployment = get_azure_openai_client()

def initial_code_request():
    print("\n STEP 1: INITIAL CODE REQUEST")

    prompt = "Create a simple Python function to calculate the area of a rectangle"

    response = create_chat_completion(
        client,
        deployment,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    initial_code = response.choices[0].message.content
    print("Initial Code:")
    print(initial_code)
    return initial_code

def refine_code_request(initial_code):
    print("\n Step 2: Ask AI to improve the code")

    refine_prompt = f"""Here's some Python code:

{initial_code}

Please suggest 3 specific improvements to make this code better. Consider:
1. Error handling
2. Documentation
3. Code structure/best practices

Then provide the improved version."""
    
    response = create_chat_completion(
        client,
        deployment,
        messages=[{"role": "user", "content": refine_prompt}],
        temperature=0.3
    )

    print("AI Improvements")
    print(response.choices[0].message.content)


if __name__ == "__main__" :
    initial_code = initial_code_request()
    refine_code_request(initial_code)
