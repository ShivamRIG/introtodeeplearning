from openai import OpenAI

class LLMClient: 
    def __init__(self, model: str, api_key: str, api_base: str = "https://openrouter.ai/api/v1"):
        self.llm_client = OpenAI(api_key=api_key, base_url=api_base)
        self.model = model

    def ask(self, user: str, system: str = None, **kwargs):
        messages = [{"role": "user", "content": user}]
        if system:
            messages.insert(0, {"role": "system", "content": system})
        res = self.llm_client.chat.completions.create(
            model=self.model,
            messages=messages,
            **kwargs
        )
        return res


yoda_test_text = (
    "Wisdom, sought by many, found by few, it is. Haste not, patience have. "
    "For in stillness, answers come. Much to learn, still you have. "
    "Fear leads to anger; anger, to hate. Down the dark path, guide you it will. "
    "Trust the Force, you must. Powerful ally it is. Life it creates, surrounds, binds. "
    "Adventure, excitement, a Jedi craves not these things. Discipline, balance, seek you should. "
    "Hmm, clearer now is the path, yes? Help you more, I can, if needed it is. "
    "Endless, the journey of learning is. Stay true to your path, and clarity you will find. "
    "Remember, the Force flows through all, but your heart determines how it shapes your destiny. "
    "Much more to teach, I have. Ready, are you? Mmm."
)



# class Llama(LLMClient):
#     def __init__(self, api_key: str):
#         """
#         Initialize the LlamaFree model client. 

#         LlamaFree is available from LlamaFree. 
#         Provide your LlamaFree API key (`api_key`) to access.
#         """
#         # super().__init__(model="meta-llama/llama-3.2-3b-instruct", api_key=api_key)
#         super().__init__(model="meta-llama/llama-3.1-8b-instruct", api_key=api_key)


# class LFM40B(LLMClient):
#     def __init__(self, api_key: str):
#         """
#         Initialize the LFM-40B model client. 

#         LFM-40B is available from Lambda Labs. 
#         Provide your Lambda Labs API key (`api_key`) to access.
#         """ 
#         api_base = "https://api.lambdalabs.com/v1"
#         super().__init__(model="lfm-40b", api_base=api_base, api_key=api_key)
