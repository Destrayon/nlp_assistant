# NLP User Assistant

*This project was made originally to be a base for creating home assistant features such as controlling the temperature or handling lighting and home security, but deciding this project could be used in a more general purpose fashion.*

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [How to Extend the Project](#how-to-extend-the-project)
- [Contribute](#contribute)
- [License](#license)
- [Contact](#contact)

## Installation

To set up this project locally for development or testing purposes, please follow the steps outlined below:

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/Destrayon/nlp_assistant.git
   ```

2. **Navigate to the Project Directory**:  
   ```bash
   cd nlp_assistant
   ```

3. **Set Up a Virtual Environment**:  
   To create an isolated environment for the project, run:  
   ```bash
   python -m venv .venv
   ```

4. **Activate the Virtual Environment**:  
   - **On Windows**:  
     ```bash
     .venv\Scripts\activate
     ```
   - **On MacOS and Linux**:  
     ```bash
     source .venv/bin/activate
     ```

5. **Install Required Packages**:  
   With the virtual environment activated, install the necessary packages using:  
   ```bash
   pip install -r requirements.txt
   ```

## Getting Started

To get the project up and running:

1. **Copy the Template Configuration**:  
   Copy the template provided in `settings.template.yml` to a new file named `settings.yml`:
   ```bash
   cp settings.template.yml settings.yml
   ```

2. **Fill in the Configuration**:  
   In the `settings.yml` file, set the `open_ai_key` field with your personal OpenAI key.

3. **Run the Main Script**:  
   Execute the `main.py` script to test the program:  
   ```bash
   python main.py
   ```
## How to Extend the Project

Our project has been structured with extensibility in mind. Here's how you can further enhance its capabilities:

### 1. Creating a New Assistant Instruction

Our system can be instructed to adapt its behavior. To create a new set of instructions for the assistant:

- **Instruction File**: Navigate to the `assistant_instructions` folder and create a new `[name].yml` file. This file will dictate how the assistant should respond.

    **Template for a new instruction file:**
    ```yml
    instructions:
        description: <Describe the instruction briefly>
        examples:
            <example_name>:
                user: <User's expected input>
                assistant: <Assistant's expected response>
    ```
    For reference on formatting, review the `default.yml` file.

    **Naming Examples**: The example identifiers (like `<example_name>`) can be any descriptive term you prefer.

- **Activate the Instruction**: After setting up a new instruction file, modify the `settings.yml` to activate it:
    ```yml
    settings:
        current_assistant_instructions: [name]
    ```

### 2. Creating a New Mod

Mods allow you to add custom functionalities. To create a new mod:

1. **Set Up Mod Directory**:  
    Navigate to the `mods` directory and create a new folder for your mod:
    ```bash
    cd mods
    mkdir [mod_name]
    ```

2. **Add Necessary Files**:  
    Your mod requires two files - `source.py` and `config.yml`. 

    - **`source.py`**:
      Here's a basic structure:
      ```python
      def name_of_function(param_name):
          # Your function's implementation here
      ```

    - **`config.yml`**:
      This configuration file connects your function to the main system. Use this template:
      ```yml
      endpoints:
        <name_of_function>:
            parameters:
                param_name: string  # Describe the parameter's type
            description: <Brief description of the function>
      ```
    **Note**: The function name in `config.yml` should match the function's name in `source.py`. Descriptive comments for parameters help the NLP to infer the correct datatypes.

3. **Integration**: Once set up, the main API will automatically detect and make your endpoint available. Ensure your mod's documentation provides ample context and use-case scenarios.

## Contribute

We welcome contributions from the community! Whether it's bug reporting, feature requests, or direct code contributions, your efforts will be appreciated. Here are some general guidelines:

1. **Bug Reporting**:  
    - If you find a bug, please create an issue detailing the problem, steps to reproduce, and expected versus actual behavior.
    - Please check existing issues to see if your bug has already been reported.

2. **Feature Requests**:  
    - Feel free to suggest new features by opening an issue.
    - Clearly describe the feature and its potential benefits.

3. **Code Contributions**:  
    - If you wish to contribute code, please fork the repository and open a pull request.
    - Ensure that your code adheres to existing style conventions within the project.
    - Include appropriate tests and documentation.

**Note**: We're still refining our contribution process. Your patience and feedback will help us create a better system. If you have suggestions for improving our guidelines or processes, please share!

## License

This project is licensed under the MIT License.

### MIT License

```
MIT License

Copyright (c) 2023 Destrayon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

By using, copying, or modifying this project, you agree to the terms stipulated in the MIT License. Ensure to always include the license text when distributing or using portions of this project to maintain compliance.

## Contact

To get in touch, view more of my work, or discuss this project:

- **GitHub**: [Destrayon](https://github.com/Destrayon)

Please use GitHub for all project-related communications. Whether you have questions, feedback, or are looking to contribute, GitHub is the preferred platform. This helps centralize discussions and ensures timely responses.
