# llama-tokens
A Quick Library with Llama 3.1 &amp; 3.2 Tokenization

To test on Terminal:
```
pip install llama-tokens
git clone https://github.com/jeffxtang/llama-tokens
cd llama-tokens
python test.py
```
You should see the output:
```
Text:  Hello, world!
Number of tokens:  4
Tokens:  ['Hello', ',', ' world', '!']
```


To test on Colab:
```
!pip install llama-tokens

!wget https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3/api/tokenizer.model

from llama_tokens import LlamaTokenizer

tokenizer = LlamaTokenizer()
text = "Hello, world!"
print("Text: ", text)
print("Number of tokens: ", tokenizer.num_tokens(text))
print("Tokens: ", tokenizer.tokens(text))
```

The same output will be generated:
```
Text:  Hello, world!
Number of tokens:  4
Tokens:  ['Hello', ',', ' world', '!']
```
