# Tokompiler: Code-Oriented Tokenizer
Tokompiler is a specialized tokenizer designed for code preprocessing and tokenization. It provides a pipeline for converting source code into a format that enhances code representation and understanding. Its primary purpose is to support the pretraining of language models for high-performance computing.

## Getting Started
To use Tokompiler, follow these steps:

Install tree-sitter:
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
