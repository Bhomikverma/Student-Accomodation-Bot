import gradio as gr
import json
from datetime import datetime
from chatbot import chat_with_bot  

# 1) Function to save the chat history
def save_chat(history):
    try:
        # history is a list of (user, bot) tuples
        formatted = []
        for user_msg, bot_msg in history:
            formatted.extend([
                {"role": "user", "content": user_msg},
                {"role": "assistant", "content": bot_msg}
            ])

        full_chat = {
            "system_prompt": "You are AccomBot, a helpful assistant for student accommodation.",
            "conversation": formatted
        }

        # unique filename
        filename = f"chatlog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(full_chat, f, indent=2)

        return f"✅ Chat saved as `{filename}`"
    except Exception as e:
        return f"Error saving chat: {e}"

# ————————————————
# 2) Function to handle user ↔️ bot turns
def respond(message, history):
    # call your chatbot logic
    bot_reply = chat_with_bot(message, history)
    # store this turn
    history.append((message, bot_reply))
    # return updated chat (for display) + clear the input box
    return history, ""

# ————————————————
# 3) Build the Gradio interface
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()                         # chat display
    user_input = gr.Textbox(                       # where i type
        placeholder="Type your message here and press Enter",
        show_label=False
    )
    save_button = gr.Button("💾 Save Chat")        # save button
    save_status = gr.Markdown()                    # save result

    # wire up the chat turn
    user_input.submit(
        fn=respond, 
        inputs=[user_input, chatbot], 
        outputs=[chatbot, user_input]
    )

    # wire up the save button
    save_button.click(
        fn=save_chat, 
        inputs=[chatbot], 
        outputs=[save_status]
    )

demo.launch()
