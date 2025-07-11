from azure_client import get_azure_openai_client, create_chat_completion

#Initilaize client
client, deployment = get_azure_openai_client()

def without_chain_of_thought():
    print("\n Without using chain of thought")

    prompt = "Sarah has 15 apples. She gives 4 to John, eats 3 herself, and then buys 7 more. How many apples does Sarah have now?"

    response = create_chat_completion(
        client, 
        deployment, 
        [{"role": "user", "content": prompt}], 
        temperature=0.1
    )

    print(f"prompt: {prompt}")
    print(f"Answer: {response.choices[0].message.content} ")

def with_chain_of_thought():
    print("\n WIth Chain of Thought")

    prompt = """Lisa has 7 apples, throws 1 apple, gives 4 apples to Bart and Bart gives one back:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice has 5 apples, throws 3 apples, gives 2 to Bob and Bob gives one back, how many apples does Alice have?
  """
    response = create_chat_completion(
        client,
        deployment,
        [{"role": "user", "content": prompt}], 
        temperature=0.1
    )
    print(f"prompt: {prompt}")
    print(f"Answer: {response.choices[0].message.content} ")

if __name__== "__main__":
    without_chain_of_thought()
    with_chain_of_thought()