# VOICE-CONTROLLED-CHATBOT
This project is a voice-controlled chatbot that interacts with the Flow GPT website. It uses speech recognition to interpret voice commands, converts them into text, and automates browser actions using Selenium. The chatbot responds to the user through a text-to-speech engine.
Developed a voice-controlled chatbot using Selenium and Speech Recognition for web automation and natural language processing.

## Features

- **Voice Recognition**: Recognizes spoken words using the `speech_recognition` library.
- **Text-to-Speech**: Converts text responses to speech using `pyttsx3`.
- **Web Automation**: Interacts with the Flow GPT website using Selenium.

## Requirements

To run this project, you need the following dependencies:

- **Python 3.x**
- **Selenium**: For browser automation.
- **pyttsx3**: For text-to-speech functionality.
- **speech_recognition**: For converting speech to text.
- **Microsoft Edge WebDriver**: Selenium WebDriver for Microsoft Edge.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/sachinchaunal/VOICE-CONTROLLED-CHATBOT.git
    cd VOICE-CONTROLLED-CHATBOT
    ```

2. **Install Dependencies**:
    Ensure you have Python 3.x installed. Then, install the required Python packages:
    ```bash
    pip install selenium pyttsx3 SpeechRecognition webdriver_manager
    ```

3. **WebDriver Setup**:
    The project uses the Microsoft Edge browser for automation. Ensure that you have Edge installed, and the `webdriver_manager` package will handle downloading the appropriate WebDriver:
    ```bash
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    ```

## Configuration

Before running the script, you need to configure the XPath for the Flow GPT website. This is necessary for the bot to correctly identify and interact with elements on the page.

1. **Find the XPath**: Open the Flow GPT website in your browser, inspect the elements you need to interact with, and copy their XPaths.
2. **Update the Script**: Modify the script to use your XPaths for interacting with the required elements.

## Usage

To start the voice-controlled chatbot, run the script:

```bash
python VOICE-CONTROLLED-CHATBOT.py
```

The chatbot will start listening for your voice commands and interact with the Flow GPT website accordingly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
