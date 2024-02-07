                                                                                                          **Gradio Chatbot Usage**

This project involves a chatbot application integrated with a Gradio application that takes user input, performs a specific action and returns the results. 
This custom application translates the user input into English, sends it to the Gradio application, and translates the response back into Turkish and presents it to the user.


**Features**

**_Language Translation:_** Automatically translates user input into English and translates responses from the Gradio app into Turkish.
**_Gradio Integration:_** Connects to the Gradio application over HTTP and processes user input.
**_Flexible Usage_:** Users can use the 'exit' command when they want to quit.


**Installation**
Before using this project, you need to prepare your system by following the steps below:

**Install the Required Libraries:**
You need gradio_client and deep_translator libraries to run the project. You can install these libraries with the following command:

bash
Copy code
pip install gradio_client deep_translator
**_URL of the Gradio App:_**
This script needs the URL of a Gradio application to run. **For example:** https://hysts-mistral-7b.hf.space/--replicas/ezo3j/

**Usage**
**_Initializing the Code:_**
Run the python file via terminal or command line to run the script.

**_User Input:_**
The user enters the desired message through the terminal.

**_Exiting:_**
When the user wants to end the chat, they can exit the application by typing 'exit'.

**_License:_**
This project is licensed under the MIT License.
