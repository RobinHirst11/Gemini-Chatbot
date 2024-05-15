## Gemini Therapist Discord Bot

This bot leverages the power of Google's Gemini language model to provide a conversational experience within a Discord server. It allows users to have open-ended conversations with the model, engaging in a variety of topics and receiving responses based on its vast knowledge base.

**Features:**

* **Direct Messaging:** The bot facilitates private conversations between users and the Gemini model.
* **Open-Ended Conversations:** Engage in natural, flowing dialogue on any subject.
* **Contextual Understanding:** The model can remember previous messages within a conversation, providing a more natural and interactive experience.
* **Safety Settings:**  The code incorporates safety settings to mitigate potential risks associated with language models, ensuring responsible and ethical usage.

**Getting Started:**

1. **Setup Environment Variables:**
   * **`GEMINI_API_KEY`:**  Obtain your API key from Google Cloud [https://cloud.google.com/generative-ai/docs/quickstart](https://cloud.google.com/generative-ai/docs/quickstart).
   * **`DISCORD_TOKEN`:** Create a Discord bot and obtain its token [https://discord.com/developers/docs/intro](https://discord.com/developers/docs/intro).

2. **Install Dependencies:**
   ```bash
   pip install discord.py google-generativeai
   ```

3. **Run the Bot:**
   ```bash
   python main.py
   ```

**Usage:**

* **Start a Chat:**
    * Send a direct message to the bot.
    * Type `/chat` followed by your initial message to start a conversation.

**Example:**

```
> /chat Hi, how are you today?
```

The bot will respond with a message, and you can continue the conversation naturally.

**Note:** This project is still under development and may have limitations. It's important to use the bot responsibly and avoid sharing sensitive information.

**License:**

This project is licensed under the Fuck You License.

**Contributions:**

Contributions are welcome! Feel free to fork the repository and submit pull requests.
