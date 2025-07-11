from azure_client import get_azure_openai_client, create_chat_completion

# Initialize client
client, deployment = get_azure_openai_client()

def test_zero_shot():
    print("\n Zero Shot Prompting")

    prompt = "What is Machine Learning"
    response = create_chat_completion(
        client, 
        deployment, 
        [{"role": "user", "content": prompt}], 
        temperature=0.7
    )
    print(f"Prompt: {prompt}")
    print(f"Response: {response.choices[0].message.content}")

def test_few_shot():
    print("\n Few Shot Prompting")

    messages = [
        {"role": "user", "content": "Explain the following machine learning concepts in one sentence."},
        {"role": "user", "content": "Supervised Learning => Training a model on labeled data to make predictions or classifications."},
        {"role": "user", "content": "Unsupervised Learning => Finding patterns or groupings in data without labeled responses."},
        {"role": "user", "content": "Reinforcement Learning => Learning to make decisions by receiving rewards or penalties for actions."},
        {"role": "user", "content": "Overfitting =>"}
    ]
    response = create_chat_completion(
        client, 
        deployment, 
        messages, 
        temperature=0.7
    )
    print("Prompt: Explain machine learning concepts in one sentence\nExamples provided.")
    print(f"Response: {response.choices[0].message.content}")

if __name__ == "__main__":
    test_zero_shot()
    test_few_shot()