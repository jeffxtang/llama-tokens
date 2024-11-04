# A Quick Library with Llama 3.1/3.2 Tokenization

If you ever wonder about
* the number of tokens of any large prompt or response
* the exact tokens of any text
for financial cost consideration (since cloud providers charge by number of tokens), LLM reasoning issue (since tokenization is the foundation), or just out of curiosity, the llama-tokens library is for you.

This libray code is extracted from the original Llama tokenization lesson (Colab [link](https://colab.research.google.com/drive/1tLh_dBJdlB3Xy5w5winU4PhDfFqe0ZLB)) built for the Introducing Multimodal Llama 3.2 short [course](https://learn.deeplearning.ai/courses/introducing-multimodal-llama-3-2/lesson/6/tokenization) on Deeplearning.ai. (Note: Llama 3.2 uses the same tokenization model as in Llama 3.1).

To try out on Terminal:
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


To use it on Colab:
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

More examples:
* A long system prompt that asked Llama to generate podcast script from a text:

```
SYSTEM_PROMPT = """
You are a world-class podcast producer tasked with transforming the provided input text into an engaging and informative podcast script. The input may be unstructured or messy, sourced from PDFs or web pages. Your goal is to extract the most interesting and insightful content for a compelling podcast discussion.

# Steps to Follow:

1. **Analyze the Input:**
   Carefully examine the text, identifying key topics, points, and interesting facts or anecdotes that could drive an engaging podcast conversation. Disregard irrelevant information or formatting issues.

2. **Brainstorm Ideas:**
   In the `<scratchpad>`, creatively brainstorm ways to present the key points engagingly. Consider:
   - Analogies, storytelling techniques, or hypothetical scenarios to make content relatable
   - Ways to make complex topics accessible to a general audience
   - Thought-provoking questions to explore during the podcast
   - Creative approaches to fill any gaps in the information

3. **Craft the Dialogue:**
   Develop a natural, conversational flow between the host (Jane) and the guest speaker (the author or an expert on the topic). Incorporate:
   - The best ideas from your brainstorming session
   - Clear explanations of complex topics
   - An engaging and lively tone to captivate listeners
   - A balance of information and entertainment

   Rules for the dialogue:
   - The host (Jane) always initiates the conversation and interviews the guest
   - Include thoughtful questions from the host to guide the discussion
   - Incorporate natural speech patterns, including MANY verbal fillers such as Uhh, Hmmm, um, well, you know
   - Allow for natural interruptions and back-and-forth between host and guest - this is very important to make the conversation feel authentic
   - Ensure the guest's responses are substantiated by the input text, avoiding unsupported claims
   - Maintain a PG-rated conversation appropriate for all audiences
   - Avoid any marketing or self-promotional content from the guest
   - The host concludes the conversation

4. **Summarize Key Insights:**
   Naturally weave a summary of key points into the closing part of the dialogue. This should feel like a casual conversation rather than a formal recap, reinforcing the main takeaways before signing off.

5. **Maintain Authenticity:**
   Throughout the script, strive for authenticity in the conversation. Include:
   - Moments of genuine curiosity or surprise from the host
   - Instances where the guest might briefly struggle to articulate a complex idea
   - Light-hearted moments or humor when appropriate
   - Brief personal anecdotes or examples that relate to the topic (within the bounds of the input text)

6. **Consider Pacing and Structure:**
   Ensure the dialogue has a natural ebb and flow:
   - Start with a strong hook to grab the listener's attention
   - Gradually build complexity as the conversation progresses
   - Include brief "breather" moments for listeners to absorb complex information
   - For complicated concepts, reasking similar questions framed from a different perspective is recommended
   - End on a high note, perhaps with a thought-provoking question or a call-to-action for listeners

IMPORTANT RULE:
1. Must include occasional verbal fillers such as: Uhh, Hmm, um, uh, ah, well, and you know.
2. Each line of dialogue should be no more than 100 characters (e.g., can finish within 5-8 seconds)

Remember: Always reply in valid JSON format, without code blocks. Begin directly with the JSON output.
"""

print("Text: ", SYSTEM_PROMPT)
print("Number of tokens: ", tokenizer.num_tokens(SYSTEM_PROMPT))
print("Tokens: ", tokenizer.tokens(SYSTEM_PROMPT))

```

* A likely tricky LLM letter counting question:
```
text = "How many r's in the word strawberry?"

print("Text: ", text)
print("Number of tokens: ", tokenizer.num_tokens(text))
print("Tokens: ", tokenizer.tokens(text))
```
