
# **AI-Chat-Eval**

AI-Chat-Eval is a Python package designed to help developers evaluate their AI chatbot systems. It provides tools for generating role-based personas and simulating conversations with those personas, enabling a structured approach to assessing chatbot performance and behavior.

---

## **Features**

- **Easy Initialization**: Start with a simple `Client` object.
- **Persona Generation**: Create detailed personas for evaluating specific use cases.
- **Conversation Simulation**: Use personas to simulate conversations and evaluate chatbot responses.
- **Extensible Design**: Modular utilities for further customization and enhancements.

---

## **Local Usage**

This project is not yet deployed to PyPI. You can test and use it locally by importing it as a module directly.

### **1. Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/Zsunwork/ai-chat-eval
cd ai-chat-eval
```

### **2. Use in a Script or Notebook**

To use the package locally, ensure your working directory is set correctly, and the `AIChatEval` folder is recognized as a module.

#### **Run from the Parent Directory**
If you are running scripts or a notebook from the `AI-Chat-Eval` root directory, you can directly import the package:

```python
from AIChatEval import Client

# Initialize the client
client = Client(key="your_api_key")

# Generate a persona
persona = client.build_persona("A student interested in AI.")
print(persona)

# Simulate a conversation
conversation = client.conversation(persona)
response = conversation.generate("What should I learn to get started?")
print(response)
```

#### **Run from a Subdirectory (e.g., `examples/`)**
If you're running from a subdirectory like `examples/`, you need to adjust the Python path to include the parent directory:

```python
import sys
import os

# Dynamically add the root path to sys.path
current_dir = os.getcwd()
root_dir = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.insert(0, root_dir)

# Now you can import the package
from AIChatEval import Client

# Initialize the client
client = Client(key="your_api_key")

# Generate a persona
persona = client.build_persona("A student interested in AI.")
print(persona)

# Simulate a conversation
conversation = client.conversation(persona)
response = conversation.generate("What should I learn to get started?")
print(response)
```

---

## **Repository Structure**

The project is organized as follows:

```plaintext
AI-CHAT-EVAL/
├── AIChatEval/               # Main package
│   ├── __init__.py           # Exposes the Client class
│   ├── _core.py              # Core logic for the Client
│   ├── _persona.py           # Persona generation module
│   ├── _conversation.py      # Conversation simulation module
│   ├── utils/                # Utility functions (logging, storage, etc.)
├── examples/                 # Usage examples
│   ├── generate_role_card.py # Example of persona generation
│   ├── simulate_chat.py      # Example of conversation simulation
│   ├── test.ipynb            # Jupyter notebook for testing
├── tests/                    # Unit tests
├── docs/                     # Documentation
├── data/                     # Example or test data
├── LICENSE                   # License file
├── pyproject.toml            # Modern packaging metadata
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies
├── setup.py                  # Installation script
```

---

## **How It Works**

### **1. Persona Generation**
- **Input**: A natural language description of a persona.
- **Output**: A structured persona object with attributes like description and traits.
- **Implementation**: The `build_persona` method in `_persona.py`.

### **2. Conversation Simulation**
- **Input**: A persona and user input text.
- **Output**: A simulated response from the persona.
- **Implementation**: The `conversation` method in `_conversation.py`.

### **3. Extensible Design**
- **Core Class**: `Client` in `_core.py`, which acts as the main interface.
- **Utilities**: Add additional utilities or functionality under `utils/`.

---

## **Development**

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI-Chat-Eval.git
   cd AI-Chat-Eval
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Testing Without Installation**
You can run examples or test scripts directly without installing the package. For instance:

#### Example of Persona Generation
```bash
python examples/generate_role_card.py
```

#### Example of Conversation Simulation
```bash
python examples/simulate_chat.py
```

### **Running Tests**
Run all unit tests to ensure everything is working correctly:

```bash
pytest tests/
```

### **Editable Mode (Optional)**
If you prefer to avoid modifying `sys.path` manually, you can install the package in editable mode for development:

```bash
pip install -e .
```

Then, you can directly import the package in scripts and notebooks:

```python
from AIChatEval import Client
```

---

## **Maintaining the Project**

### **Adding Features**
- Extend the `Client` class in `_core.py` or add new modules under `AIChatEval/`.
- Update examples and documentation to reflect new functionality.

### **Code Quality**
- Follow [PEP 8](https://pep8.org/) for consistent code style.
- Use linters like `flake8` or formatters like `black`.

### **Documentation**
- Document public methods in the code using docstrings.
- Update `README.md` to reflect any major changes.

---

## **Contributing**

We welcome contributions! Follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes and push them to your fork.
4. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
