from pathlib import Path

import tiktoken
from tiktoken.load import load_tiktoken_bpe


class LlamaTokenizer:
    def __init__(self):
        tokenizer_path = "./tokenizer.model"
        num_reserved_special_tokens = 256

        mergeable_ranks = load_tiktoken_bpe(tokenizer_path)

        num_base_tokens = len(mergeable_ranks)
        special_tokens = [
            "<|begin_of_text|>",
            "<|end_of_text|>",
            "<|reserved_special_token_0|>",
            "<|reserved_special_token_1|>",
            "<|finetune_right_pad_id|>",
            "<|step_id|>",
            "<|start_header_id|>",
            "<|end_header_id|>",
            "<|eom_id|>",
            "<|eot_id|>",
            "<|python_tag|>",
            "<|image|>",
        ]

        reserved_tokens = [
            f"<|reserved_special_token_{2 + i}|>"
            for i in range(num_reserved_special_tokens - len(special_tokens))
        ]
        special_tokens = special_tokens + reserved_tokens

        # source: https://github.com/meta-llama/llama-models/blob/main/models/llama3/api/tokenizer.py#L53
        self.tokenizer = tiktoken.Encoding(
            name=Path(tokenizer_path).name,
            pat_str=r"(?i:'s|'t|'re|'ve|'m|'ll|'d)|[^\r\n\p{L}\p{N}]?\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]+[\r\n]*|\s*[\r\n]+|\s+(?!\S)|\s+",
            mergeable_ranks=mergeable_ranks,
            special_tokens={
                token: len(mergeable_ranks) + i
                for i, token in enumerate(special_tokens)
            },
        )

    def num_tokens(self, text: str) -> int:
        """Return the number of tokens in the text string."""
        return len(self.tokenizer.encode(text))

    def tokens(self, text: str) -> str:
        """Return the tokens of the text string."""
        encoded_tokens = self.tokenizer.encode(text)
        return [self.tokenizer.decode([token]) for token in encoded_tokens]


if __name__ == "__main__":
    tokenizer = LlamaTokenizer()
    text = "Hello, world!"
    print("Text: ", text)
    print("Number of tokens: ", tokenizer.num_tokens(text))
    print("Tokens: ", tokenizer.tokens(text))
