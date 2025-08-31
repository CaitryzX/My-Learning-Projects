# NEW Programming Vocabulary & Concepts

print("=== NEW PROGRAMMING VOCABULARY ===\n")

# 1. ADVANCED PYTHON CONCEPTS
print("1. ADVANCED PYTHON CONCEPTS")
print("=" * 40)

concepts = {
    "List Comprehension": "Creating lists using compact syntax: [x**2 for x in range(5)]",
    "Lambda Function": "Anonymous function: lambda x: x*2",
    "Decorator": "Function that modifies another function",
    "Generator": "Function that yields values one at a time",
    "Context Manager": "Using 'with' statement for resource management",
    "Exception Handling": "Try-except blocks for error management",
    "Type Hints": "Specifying data types: def func(x: int) -> str:",
    "Docstring": "Documentation string for functions/classes"
}

for concept, explanation in concepts.items():
    print(f"📚 {concept}: {explanation}")

print("\n" + "=" * 50 + "\n")

# 2. DATA STRUCTURES
print("2. DATA STRUCTURES")
print("=" * 40)

data_structures = {
    "List": "Ordered, mutable collection [1, 2, 3]",
    "Tuple": "Ordered, immutable collection (1, 2, 3)",
    "Set": "Unordered, unique collection {1, 2, 3}",
    "Dictionary": "Key-value pairs {'name': 'John', 'age': 25}",
    "Stack": "LIFO (Last In, First Out) data structure",
    "Queue": "FIFO (First In, First Out) data structure",
    "Tree": "Hierarchical data structure",
    "Graph": "Network of connected nodes"
}

for structure, description in data_structures.items():
    print(f"🏗️  {structure}: {description}")

print("\n" + "=" * 50 + "\n")

# 3. ALGORITHM CONCEPTS
print("3. ALGORITHM CONCEPTS")
print("=" * 40)

algorithms = {
    "Sorting": "Arranging data in specific order (bubble, quick, merge)",
    "Searching": "Finding data in collection (linear, binary)",
    "Recursion": "Function calling itself",
    "Iteration": "Repeating process with loops",
    "Divide & Conquer": "Breaking problem into smaller parts",
    "Dynamic Programming": "Solving complex problems by breaking into simpler ones",
    "Greedy Algorithm": "Making locally optimal choice at each step",
    "Backtracking": "Trying different solutions and undoing if wrong"
}

for algorithm, explanation in algorithms.items():
    print(f"⚡ {algorithm}: {explanation}")

print("\n" + "=" * 50 + "\n")

# 4. SOFTWARE DEVELOPMENT TERMS
print("4. SOFTWARE DEVELOPMENT TERMS")
print("=" * 40)

dev_terms = {
    "API": "Application Programming Interface - way programs communicate",
    "Framework": "Pre-built structure for building applications",
    "Library": "Collection of pre-written code",
    "Debugging": "Finding and fixing errors in code",
    "Testing": "Checking if code works correctly",
    "Version Control": "Tracking changes in code (Git)",
    "Deployment": "Making application available to users",
    "CI/CD": "Continuous Integration/Continuous Deployment"
}

for term, meaning in dev_terms.items():
    print(f"🔧 {term}: {meaning}")

print("\n" + "=" * 50 + "\n")

# 5. WEB DEVELOPMENT CONCEPTS
print("5. WEB DEVELOPMENT CONCEPTS")
print("=" * 40)

web_concepts = {
    "Frontend": "What users see (HTML, CSS, JavaScript)",
    "Backend": "Server-side logic (Python, databases)",
    "Database": "Storing and organizing data",
    "Server": "Computer that hosts your application",
    "Client": "User's browser or device",
    "HTTP": "Protocol for web communication",
    "REST API": "Rules for building web services",
    "Authentication": "Verifying user identity"
}

for concept, description in web_concepts.items():
    print(f"🌐 {concept}: {description}")

print("\n" + "=" * 50 + "\n")

# 6. NEW PROGRAMMING PATTERNS
print("6. NEW PROGRAMMING PATTERNS")
print("=" * 40)

patterns = {
    "Singleton": "Class with only one instance",
    "Factory": "Creating objects without specifying exact class",
    "Observer": "Object notifying others of changes",
    "Strategy": "Defining family of algorithms",
    "Adapter": "Making incompatible interfaces work together",
    "Decorator": "Adding behavior to objects dynamically",
    "Command": "Encapsulating request as object",
    "Template Method": "Defining algorithm skeleton"
}

for pattern, explanation in patterns.items():
    print(f"🎯 {pattern}: {explanation}")

print("\n" + "=" * 50 + "\n")

# 7. PRACTICAL EXAMPLES
print("7. PRACTICAL EXAMPLES")
print("=" * 40)

# Example 1: List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"📊 List Comprehension Example:")
print(f"   Numbers: {numbers}")
print(f"   Even squares: {even_squares}")

# Example 2: Lambda with Map
doubled = list(map(lambda x: x * 2, numbers))
print(f"\n🔄 Lambda + Map Example:")
print(f"   Original: {numbers}")
print(f"   Doubled: {doubled}")

# Example 3: Dictionary Comprehension
word = "programming"
char_count = {char: word.count(char) for char in set(word)}
print(f"\n📝 Dictionary Comprehension Example:")
print(f"   Word: '{word}'")
print(f"   Character count: {char_count}")

print("\n" + "=" * 50)
print("🎉 Keep learning these new concepts!")
print("💡 Practice them in your projects!")
print("🚀 Build something amazing!")
print("=" * 50)
