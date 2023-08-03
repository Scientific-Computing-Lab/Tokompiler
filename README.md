<<<<<<< HEAD
# Tokompiler
Peplexity calculation in acordance to polycoder (https://arxiv.org/abs/2202.13169) methods using lmppl (https://github.com/asahi417/lmppl)

you will need your model in the huggingface format. preferbly pytorch only.

## enviorment
the environment.yml just works.
but if you already have pytorch installed using the partial_requirments.txt with pip works just fine.

## Usage

After setting up your environment and ensuring you have a compatible model, you can calculate perplexity by running the perplexity.py script with your chosen model and text inputs. 

Here is an example of how to use the script:

```python

# Get lexical count for the texts using 'c' language lexer (replace 'c' with the appropriate lexer for your texts)
count = get_lex_count(texts,'c')

tokenizer=AutoTokenizer.from_pretrained('gpt2')
model=AutoModelForCausalLM.from_pretrained('gpt2')
scorer = lmppl_code.LM(tokenizer=tokenizer, model_obj=model)
print(scorer.get_perplexity(texts,count))
```
pip install tree-sitter
```


Build the Tree-sitter parser by executing the following commands from the root directory:

```
cd parsers
python build_ts.py
```

## Pipeline Overview
The pipeline of using Tokompiler consists of the following steps:

1. Convert Representation
The ConvertRepresentation class contains a function called generate_replaced that takes input code and the programming language. It returns a replaced format of the code. For example:

Original Code:
```
int main() {
    int r[2800 + 1];
    // ... (code continues)
}
```

Replaced Format:
```
int func_252() {
    int arr_88[num_34 + num_842];
    // ... (replaced code)
}
```

2. Lexicalization
The Lexicalization class contains a function called lexicalize that splits the code into its semantical tokens given the code and the programming language. For example:

Original Code:
```
int func_252() {
    int arr_88[num_34 + num_842];
    // ... (code continues)
}
```

Lexicalized Tokens:
```
["int", "func", "252", "(", ")", "{", "int", "arr", "88", // ... (tokens continue)
```

3. Tokenization
The Tokenizer class defines an interface that Tokompiler implements. It includes the following functions:

tokenize: Converts code into a list of tokens.

encode: Given code, returns a list of IDs representing each token.

decode: Given a list of token IDs, returns the original code.


## Example Usage
A complete example of using Tokompiler can be found in [this example script](https://github.com/Scientific-Computing-Lab-NRCN/Tokompiler/blob/main/example.py).
>>>>>>> main
