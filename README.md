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

# Calculate and print decoder only perplexity using 'gpt2' model
print(decoder_only_perplexity(texts,'gpt2',count))

# Calculate and print encoder-decoder perplexity using 'google/flan-t5-small' model
print(encoder_decoder_perplexity(texts,'google/flan-t5-small',count))
'''