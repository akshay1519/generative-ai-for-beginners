from azure_client import get_azure_openai_client, create_chat_completion

client, deployment = get_azure_openai_client()

def generated_knowledge_prompt():
    print("\n GENERATED KNOWLEDGE PROMPT")

    company_data = {
        "company": "TechMart Electronics",
        "products" : [
            {"name": "StudentBook Pro", "price": "$599", "specs": "8GB RAM, 256GB SSD, 13-inch"},
            {"name": "BudgetMax Laptop", "price": "$399", "specs": "4GB RAM, 128GB SSD, 14-inch"},
            {"name": "PowerHouse Elite", "price": "$1299", "specs": "16GB RAM, 512GB SSD, 15-inch"}
        ],

        "budget": "$600",
        "requirements": "programming, note-taking, portable,Heavy task"
    }

    prompt = f"""Company: {company_data['company']}
Available Laptops:
- {company_data['products'][0]['name']}: {company_data['products'][0]['price']}, {company_data['products'][0]['specs']}
- {company_data['products'][1]['name']}: {company_data['products'][1]['price']}, {company_data['products'][1]['specs']}  
- {company_data['products'][2]['name']}: {company_data['products'][2]['price']}, {company_data['products'][2]['specs']}

Customer Budget: {company_data['budget']}
Requirements: {company_data['requirements']}

Based on the budget and requirements, recommend the best laptop from our inventory and explain why."""
    
    response = create_chat_completion(
       client,
       deployment,
       messages=[{"role": "user", "content": prompt}],
       temperature=0.3
    )

    print("Company-specific recommendation:")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    generated_knowledge_prompt()