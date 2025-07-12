from azure_client import get_azure_openai_client,create_chat_completion

client, deployment = get_azure_openai_client()

def test_different_temperatures():
    print("\n Test same prompt with different temperature settings")

    prompt = "Write a short story about a robot learning to paint"
    temperatures = [0.1, 0.7, 0.9]

    for temp in temperatures:
        print(f"\n TEMPERATURE: {temp}")

        response = create_chat_completion(
            client,
            deployment,
            messages=[{"role": "user", "content": prompt}],
            temperature=temp
        )

        print(f"Story (temp={temp}):")
        print(response.choices[0].message.content[:200] + "...")


if __name__ == "__main__":
    test_different_temperatures()