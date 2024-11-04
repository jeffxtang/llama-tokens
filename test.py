from llama_tokens import LlamaTokenizer

tokenizer = LlamaTokenizer()
text = "Hello, world!"
print("Text: ", text)
print("Number of tokens: ", tokenizer.num_tokens(text))
print("Tokens: ", tokenizer.tokens(text))
