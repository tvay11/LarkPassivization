# LarkPassivization

A Python-based tool for transforming active-voice sentences into passive voice using natural language processing and syntactic analysis.

## Project Overview

LarkPassivization is a focused utility that automates the conversion of English sentences from active to passive voice. Built on top of the Lark parsing library, the project demonstrates a practical application of context-free grammars and syntactic tree manipulation for natural language transformation tasks. The tool is designed for writers, editors, and developers who need to analyze or rewrite sentence structures programmatically.

The project addresses a common challenge in natural language processing: performing accurate grammatical transformations while preserving the original meaning. By leveraging a formal grammar definition and a custom transformation engine, LarkPassivization provides a deterministic and transparent approach to voice conversion, making it a useful reference for those exploring computational linguistics or grammar-based text processing.

## Core Features

- **Active-to-Passive Conversion**: Transforms sentences from active voice to passive voice using rule-based syntactic analysis.
- **Grammar-Driven Parsing**: Employs a context-free grammar defined with Lark to parse English sentence structures accurately.
- **Syntactic Tree Manipulation**: Modifies parse trees to rearrange subject, verb, and object components according to passive voice rules.
- **Support for Common Sentence Patterns**: Handles simple declarative sentences with transitive verbs, including tense and agreement adjustments.
- **Modular Codebase**: Separates grammar definition, parsing logic, and transformation rules into distinct, reusable modules.
- **Command-Line Interface**: Provides a straightforward CLI for processing individual sentences or batch input from files.

## Technology Stack

- **Python**: Chosen for its readability, extensive standard library, and strong ecosystem for text processing and natural language tasks. Python's dynamic typing and rapid prototyping capabilities made it ideal for iterating on grammar rules and transformation logic.
- **Lark**: A powerful parsing library that enables the definition of context-free grammars in a clean, declarative syntax. Lark's ability to generate parse trees and support tree transformations directly aligns with the project's need to analyze and restructure sentence syntax.
- **Standard Library Modules**: Utilizes Python's built-in `argparse` for CLI argument handling and `json` for potential serialization of parse trees, keeping external dependencies minimal.

## Architecture and Design Decisions

The project follows a modular architecture with clear separation of concerns:

- **Grammar Module**: Contains the Lark grammar definition for English sentence structures. This module is isolated to allow easy modification or extension of the grammar without affecting other components.
- **Parser Module**: Handles the initialization of the Lark parser and provides functions to parse input sentences into syntax trees. Error handling is implemented to manage ungrammatical or unsupported input gracefully.
- **Transformer Module**: Implements the core logic for converting active-voice parse trees into passive-voice trees. This module uses Lark's `Transformer` class to traverse and modify tree nodes, ensuring that verb tense, subject-verb agreement, and prepositional phrases are handled correctly.
- **CLI Module**: Provides the user-facing interface, accepting input via command-line arguments or file paths and outputting the transformed sentences.

Design decisions include:

- **Rule-Based Approach**: Rather than relying on statistical or machine learning models, the project uses explicit grammatical rules. This ensures deterministic, explainable transformations and avoids the need for training data.
- **Minimal Dependencies**: The project intentionally limits external libraries to Lark and Python's standard library, making it easy to set up and run in any Python environment.
- **Error Resilience**: The parser includes fallback mechanisms for sentences that do not match the grammar, providing informative error messages instead of crashing.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tvay11/LarkPassivization.git
   cd LarkPassivization
   ```

2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install lark-parser
   ```

4. **Run the tool**:
   ```bash
   python main.py "The cat chased the mouse."
   ```
   Output:
   ```
   The mouse was chased by the cat.
   ```

   For batch processing from a file:
   ```bash
   python main.py --file input_sentences.txt
   ```

## Future Scope and Key Learnings

This project provided valuable experience in formal grammar design, syntactic parsing, and tree-based text transformation. Key learnings include the importance of precise grammar definitions for handling edge cases, such as irregular verb forms and complex noun phrases.

Future expansion possibilities include:

- Extending the grammar to support more complex sentence structures, such as those with auxiliary verbs, modal verbs, or embedded clauses.
- Adding support for interrogative and imperative sentences.
- Implementing a web-based interface for easier accessibility.
- Incorporating a feedback mechanism to allow users to correct or refine transformations, enabling iterative improvement of the grammar rules.

LarkPassivization serves as both a practical tool and a learning resource for anyone interested in the intersection of programming and linguistics.