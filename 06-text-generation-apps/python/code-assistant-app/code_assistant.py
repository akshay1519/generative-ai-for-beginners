import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

class CodeAssistant:
    def __init__(self):
        print("Initialize the Code Assistant with Azure OpenAI configuration")
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
        self.conversation_history = []

    def create_completion(self, messages, temperature=0.3, max_tokens=1000):
        print("Create a completion using Azure OpenAI")
        try:
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def explain_code(self, code, language="Python"):
        print("Explain how a piece of code works")

        system_prompt = f"""You are an expert {language} programmer and teacher. 
        Explain code in a clear, educational way that helps users understand:
        1. What the code does
        2. How it works step-by-step
        3. Key concepts or patterns used
        4. Any potential improvements or best practices
        
        Keep explanations beginner-friendly but technically accurate."""

        user_prompt = f"Please explain this {language} code:\n\n```{language.lower()}\n{code}\n```"
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        return self.create_completion(messages, temperature=0.2)
    
    def generate_code(self, description, language="Python", difficulty="beginer"):
        print("Generate code based on description")

        system_prompt = f"""You are an expert {language} programmer. Generate clean, well-commented code based on user requirements.
        
        Guidelines:
        - Write {difficulty}-level code
        - Include helpful comments
        - Follow {language} best practices
        - Include error handling where appropriate
        - Provide a brief explanation after the code
        """

        user_prompt = f"Create {language} code for: {description}"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        return self.create_completion(messages, temperature=0.4, max_tokens=1500)
    
    def debug_code(self, code, error_message, language="Python"):
        print("Help debug code issues")

        system_prompt = f"""You are an expert {language} debugger. Help users fix code issues by:
        1. Identifying the problem
        2. Explaining why it occurs
        3. Providing the corrected code
        4. Suggesting how to prevent similar issues
        
        Be specific and educational in your explanations."""
        
        user_prompt = f"""I'm getting an error in this {language} code:

        Error: {error_message}

        Code:
        ```{language.lower()}
        {code}
        ```

        Please help me fix this issue."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        return self.create_completion(messages, temperature=0.2, max_tokens=1200)
    
    def optimize_code(self, code, language="Python"):
        print("Suggest optimizations for existing code")

        system_prompt = f"""You are an expert {language} performance consultant. Analyze code and suggest improvements for:
        1. Performance optimization
        2. Code readability
        3. Best practices
        4. Security considerations
        
        Explain the reasoning behind each suggestion."""

        user_prompt = f"Please analyze and suggest optimizations for this {language} code:\n\n```{language.lower()}\n{code}\n```"
    
        messages = [
            {"role": "system", "content": system_prompt },
            {"role": "user", "content": user_prompt}
        ]

        return self.create_completion(messages, temperature=0.3,max_tokens=1500)
    
    def code_review(self, code, language="Python"):
        print("Perform a comprehensive code review")
        system_prompt = f"""You are a senior {language} developer conducting a code review. Evaluate the code for:
        
        1. **Functionality**: Does it work correctly?
        2. **Readability**: Is it easy to understand?
        3. **Performance**: Are there efficiency issues?
        4. **Security**: Any security vulnerabilities?
        5. **Best Practices**: Following {language} conventions?
        6. **Maintainability**: Easy to modify and extend?
        
        Provide specific, actionable feedback with examples."""
        
        user_prompt = f"Please review this {language} code:\n\n```{language.lower()}\n{code}\n```"
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        return self.create_completion(messages, temperature=0.3, max_tokens=2000)
    
    def interactive_session(self):
        print("Code Assistant Started!")
        print("Available commands:")
        print("1. 'explain' - Explain existing code")
        print("2. 'generate' - Generate new code")
        print("3. 'debug' - Help fix code issues")
        print("4. 'optimize' - Suggest code improvements")
        print("5. 'review' - Comprehensive code review")
        print("6. 'quit' - Exit the assistant")

        while True:
            command = input("\n What would you like to do? ").strip().lower()

            match command:
                case 'quit':
                    print("Thanks for using Code Assistant!")
                    break
                case 'explain':
                    self._handle_explain()
                case 'generate':
                    self._handle_generate()
                case 'debug':
                    self._handle_debug()
                case 'optimize':
                    self._handle_optimize()
                case 'review':
                    self._handle_review()
                case _:
                    print("Unknown command. Please use: explain, generate, debug, optimize, review, or quit")

    
    def _handle_explain(self):
        print("Handle code explanation requests")
        code = input("Enter the code you want to explain (or 'exit' to quit): ").strip()
        if code.lower() == 'exit':
            return

        language = input("Programming language (default: Python): ").strip() or "Python"
        explanation = self.explain_code(code, language)
        print(f"Explanation:\n{explanation}")

    
    def _handle_generate(self):
        print("Handle code generation requests")
        description = input("Describe the code you need: ").strip()
        language = input("Programming language (default: Python): ").strip() or "Python"
        difficulty = input("Difficulty level (beginner, intermediate, advanced, default: beginner): ").strip() or "beginner"

        if description:
            print("Generating code...")
            generated_code = self.generate_code(description, language, difficulty)
            print(f"Generated Code:\n{generated_code}")
        else:
            print("No description provided.")

    def _handle_debug(self):
        print("Handle code debugging requests")
        code = input("Enter the code you want to debug (or 'exit' to quit): ").strip()
        if code.lower() == 'exit':
            return

        error_message = input("Enter the error message you are encountering: ").strip()
        language = input("Programming language (default: Python): ").strip() or "Python"

        if error_message:
            print("Debugging code...")
            debugged_code = self.debug_code(code, error_message, language)
            print(f"Debugged Code:\n{debugged_code}")
        else:
            print("No error message provided.")
    
    def _handle_optimize(self):
        print("Handle code optimization requests")
        code = input("Enter the code you want to optimize (or 'exit' to quit): ").strip()
        if code.lower() == 'exit':
            return

        language = input("Programming language (default: Python): ").strip() or "Python"

        if code:
            print("Optimizing code...")
            optimized_code = self.optimize_code(code, language)
            print(f"Optimized Code:\n{optimized_code}")
        else:
            print("No code provided.")

    def _handle_review(self):
        print("Handle code review requests")
        code = input("Enter the code you want to review (or 'exit' to quit): ").strip()
        if code.lower() == 'exit':
            return

        language = input("Programming language (default: Python): ").strip() or "Python"

        if code:
            print("Reviewing code...")
            review_feedback = self.code_review(code, language)
            print(f"Code Review Feedback:\n{review_feedback}")
        else:
            print("No code provided.")

def main():
    print("Starting Code Assistant...")
    try:
        assistant = CodeAssistant()
        assistant.interactive_session()
    except Exception as e:
        print("An error occurred while starting the Code Assistant:")
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()