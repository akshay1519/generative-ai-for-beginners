from code_assistant import CodeAssistant
import os

class AdvancedCodeAssistant(CodeAssistant):
    def __init__(self):
        super().__init__()

    def generate_unit_tests(self, code, language="Python"):
        print("Generate unit tests for the given code")

        system_prompt = f"""You are an expert {language} test engineer. Generate comprehensive unit tests for the provided code.
        
        Include:
        1. Test cases for normal functionality
        2. Edge cases and boundary conditions
        3. Error handling tests
        4. Clear test names and descriptions
        5. Proper test structure and assertions

        Use appropriate testing frameworks ({language}-specific)."""

        user_prompt = f"Generate unit tests for this {language} code:\n\n```{language.lower()}\n{code}\n```"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        return self.create_completion(messages, temperature=0.4, max_tokens=2000)
    
    def convert_code(self, code, from_language, to_language):
        print(f"Convert {from_language} code to {to_language}")

        system_prompt = f"""You are an expert programmer fluent in multiple languages. Convert code from {from_language} to {to_language}.

        Guidelines:
        1. Maintain the same functionality
        2. Use {to_language} best practices and idioms
        3. Add comments explaining language-specific differences
        4. Ensure the converted code is production-ready
        5. Highlight any limitations or differences in behavior"""

        user_prompt = f"Convert this {from_language} code to {to_language}:\n\n```{from_language.lower()}\n{code}\n```"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        return self.create_completion(messages, temperature=0.3, max_tokens=2000)
    
    def create_documentation(self, code, language="Python"):
        print("Generate documentation for the given code")

        system_prompt = f"""You are a technical documentation expert. Create comprehensive documentation for the provided {language} code.

        Include:
        1. Overview and purpose
        2. Function/class descriptions
        3. Parameter explanations
        4. Return value descriptions
        5. Usage examples
        6. Code comments and docstrings
        7. Any dependencies or requirements"""

        user_prompt = f"Create documentation for this {language} code:\n\n```{language.lower()}\n{code}\n```"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        return self.create_completion(messages, temperature=0.2, max_tokens=2000)

    def suggest_architecture(self, project_description, requirements):
        print("Suggest software architecture for a project")

        system_prompt = """You are a senior software architect. Analyze project requirements and suggest appropriate architecture.

        Consider:
        1. Scalability requirements
        2. Technology stack recommendations
        3. Design patterns
        4. Database choices
        5. Security considerations
        6. Deployment strategies
        7. Code organization and structure"""
        
        user_prompt = f"""Project Description: {project_description}

        Requirements:
        {requirements}

        Please suggest an appropriate software architecture and technology stack."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        return self.create_completion(messages, temperature=0.4, max_tokens=2500)

def demo_advanced_features():
    assistant = AdvancedCodeAssistant()
    
    sample_code = """
    def calculate_fibonacci(n):
        if n <= 1:
            return n
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

    def fibonacci_sequence(length):
        sequence = []
        for i in range(length):
            sequence.append(calculate_fibonacci(i))
        return sequence
    """

    # Generate unit tests
    print("Generating unit tests...")
    unit_tests = assistant.generate_unit_tests(sample_code, language="Python")
    print(unit_tests)

    # Convert code from Python to JavaScript
    print("Converting code from Python to JavaScript...")
    converted_code = assistant.convert_code(sample_code, from_language="Python", to_language="JavaScript")
    print(converted_code)

    # Create documentation for the code
    print("Generating documentation...")
    documentation = assistant.create_documentation(sample_code, language="Python")
    print(documentation)

    # Suggest architecture for a project
    print("Suggesting architecture for a project...")
    project_description = "A web application for managing personal finances"
    requirements = "Users should be able to track expenses, set budgets, and generate reports."
    architecture_suggestion = assistant.suggest_architecture(project_description, requirements)
    print(architecture_suggestion)

if __name__ == "__main__":
    demo_advanced_features()