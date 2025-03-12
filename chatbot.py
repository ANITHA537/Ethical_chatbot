
import google.generativeai as genai


def get_response(user_input):
    prompt = f"{user_input}"
    
    
    genai.configure(api_key="AIzaSyBLF9puq46wY5MCz_NLOa8CaUQt8E49FqU")
    #print(prompt)

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
        {
        "role": "user",
        "parts": [
            "hi\n",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Hi there! How can I help you today?\n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "just creating a prompt\n",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Okay, I understand. Feel free to use me as a sounding board. If you want feedback on your prompt, just share it and I'll do my best to give you some helpful input. Good luck!\n",
        ],
        }
    ]
    )

    response = chat_session.send_message(prompt)

    #print(response.text)

    
    return response.text.strip()
