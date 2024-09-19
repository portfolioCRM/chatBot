# ChatBoot Server

The ChatBoot Server is a modular, Flask-based application designed to handle various AI-driven tasks such as model selection, user authentication, and response generation. The server leverages multiple machine learning and rule-based algorithms to provide dynamic and contextually relevant responses, making it suitable for a wide range of conversational AI applications.

## Key Features

- **Modular Architecture**: The server is structured to allow easy modifications, extensions, and maintenance. Core functionalities are divided into separate modules, each responsible for a specific aspect of the system.
  
- **Algorithm Variety**: The server incorporates a variety of algorithms, including system-based rules, multi-armed bandits, Q-networks, and content-based filtering, allowing it to adapt and optimize responses based on different strategies.

- **AI-Driven Decision Making**: It uses AI routes to select and apply the best-suited algorithms for the given context, improving the quality and relevance of interactions.

- **Scalability**: Designed with scalability in mind, the server structure allows for easy integration of new models and algorithms as the project evolves.

- **Configurable Settings**: A dedicated configuration module manages environment-specific settings, which makes the server adaptable to different deployment scenarios such as development, testing, and production.

- **Robust Error Handling and Logging**: Centralized error handling ensures that the server remains stable even when unexpected issues occur, while the logging configuration aids in monitoring and debugging.

- **Testing Suite**: The inclusion of a comprehensive testing suite with unit and integration tests ensures that the server's functionalities are thoroughly validated, enhancing reliability.

## Intended Use Cases

- **Chatbots and Virtual Assistants**: Ideal for building intelligent chatbots that require dynamic response generation.
- **Customer Support Systems**: Can be used in automated customer support systems that need to adapt responses based on historical interactions.
- **Recommendation Systems**: Suitable for use in environments where recommendations need to be generated based on user input and behavior.
- **Research and Development**: The modular design allows researchers to experiment with different algorithms and models for conversational AI.

The ChatBoot Server's flexible, robust, and scalable nature makes it an excellent choice for any AI-driven conversational application, offering a blend of traditional and cutting-edge algorithms to meet diverse requirements.

## File Structure

Below is the file structure of the project:

```
server_Flask_chat_boot/
│
│
├── routes
│ ├── ai
│ | ├── __init__.py
│ | ├── redirect_model.py
│ | └── choose_algorithm.py
│ ├── __init__.py
│ ├── health.py
│ ├── authentication.py
│ └── __init__.py
├── algorithm
│ ├── system_based_rules
│ | ├── __init__.py
│ | ├── collect_model.py
│ | └── response_model.py
│ ├── multi_armed_bandit
│ | ├── __init__.py
│ | ├── collect_model.py
│ | └── response_model.py
│ ├── Q_networks
│ | ├── __init__.py
│ | ├── collect_model.py
│ | └── response_model.py
│ ├── content_based_filtering
│ | ├── __init__.py
│ | ├── collect_model.py
│ | └── response_model.py
│ └── connect.py
├── util
│ ├── generate_response.py
│ ├── connect_to_database.py
│ └── tree_response.py
├── test
│ ├── unit_tests
│ │    ├── test_routes.py
│ │    ├── test_algorithms.py
│ │    └── test_util.py
│ └── post-man_collection.json
│
├── server.py
├── requirements.txt
├── .gitignore
└── README.md
```


## Description of Key Files and Directories

- `/routes`: This directory contains modular routing configurations for the server.
  - `ai/`: Subdirectory containing AI-related routes.
    - `__init__.py`: Initialization file for the AI routes.
    - `redirect_model.py`: Handles the redirection of models based on requests.
    - `choose_algorithm.py`: Manages the selection of appropriate algorithms for AI tasks.
  - `__init__.py`: Initialization file to recognize the `routes` directory as a package.
  - `health.py`: Manages routes related to checking the health status of the server.
  - `authentication.py`: Handles routes related to user authentication.

- `/algorithm`: Contains the core algorithms used in the project.
  - `system_based_rules/`: Subdirectory containing system-based rules algorithms.
    - `__init__.py`: Initialization file for system-based rules.
    - `collect_model.py`: Manages data collection for system-based rules.
    - `response_model.py`: Handles the generation of responses based on system rules.
  - `multi_armed_bandit/`: Subdirectory containing Multi-Armed Bandit algorithms.
    - `__init__.py`: Initialization file for Multi-Armed Bandit algorithms.
    - `collect_model.py`: Handles data collection for Multi-Armed Bandit.
    - `response_model.py`: Manages response generation for Multi-Armed Bandit.
  - `Q_networks/`: Subdirectory containing Q-learning and neural network-based algorithms.
    - `__init__.py`: Initialization file for Q-learning algorithms.
    - `collect_model.py`: Handles data collection for Q-learning networks.
    - `response_model.py`: Manages response generation for Q-learning networks.
  - `content_based_filtering/`: Subdirectory containing content-based filtering algorithms.
    - `__init__.py`: Initialization file for content-based filtering algorithms.
    - `collect_model.py`: Manages data collection for content-based filtering.
    - `response_model.py`: Handles response generation for content-based filtering.
  - `connect.py`: Script to connect and integrate various algorithm modules.

- `/util`: Includes utility scripts and helper functions.
  - `generate_response.py`: Provides functions for generating standardized responses.
  - `connect_to_database.py`: Manages database connection logic.
  - `tree_response.py`: Includes tree-based response generation functions.

- `/test`: Contains test files for the application.
  - `post-man_collection.json`: A Postman collection used for testing the API endpoints.
  - `unit_tests/`: Directory containing automated unit and integration tests.
    - `test_routes.py`: Tests for validating routes functionality.
    - `test_algorithms.py`: Tests for validating algorithm implementations.
    - `test_util.py`: Tests for validating utility functions.

- `server.py`: The main entry point for the Flask application, initializing and running the server.

- `requirements.txt`: Lists all dependencies required by the project, which need to be installed before running the server.

- `.gitignore`: Specifies files and directories to be ignored by version control (e.g., environment files).


## Usage

To run the server, execute the `server.py` file. Make sure to install the required dependencies listed in `requirements.txt`.
for more details see [Use file](USE.md)

## Testing

The `/test` directory contains test files, including a Postman collection (`post-man_collection.json`), for testing the APIs and functionalities.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).