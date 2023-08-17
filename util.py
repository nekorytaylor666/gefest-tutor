import openai
openai.api_key = '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'


def load_transcription(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def ask_gpt(question, context):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"{context}\n\nQ: {question}\nA:",
        max_tokens=150
    )
    return response.choices[0].text.strip()
