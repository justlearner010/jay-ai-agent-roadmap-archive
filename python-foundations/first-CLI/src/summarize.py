from openai import OpenAI
class OpenAILLM:
    def __init__(self):
        self.client = OpenAI()
    
    def summarize_with_llm(self,text):
        response = self.client.responses.create(
            model="gpt-5.5",
            input=f"请总结一下文本:\n{text}"
        )

        return response.output_text

class MOCKLLM:
    def summarize(self,text):
        return"fake summary"

class Summarizer:

    def __init__(self,llm):
        self.llm = llm

    def run(self, text):
        if not text.strip():
            return "No content to summarize."

        return self.llm.summarize(text)
    
def summarize_text(text, mode="brief"):

    if not text.strip():
        return "No content to summarize."

    if mode == "brief":
        return f"Brief summary: this text has {len(text.split())} words"

    if mode == "bullets":
        return [
            f"- Word count: {len(text.split())}",
            f"- Character count: {len(text)}",
            "- Mock summary: this is a placeholder summary.",
            ]

    raise ValueError("mode must be 'brief' or 'bullets'")
