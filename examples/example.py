import os
from tokompiler import convert_representation as cr
from tokompiler import lexicalize, parse_tools, Tokompiler


lang = 'fortran' 
code = str("""SUBROUTINE MySubroutine(a, b, c)
    REAL, INTENT(IN) :: a, b
    REAL, INTENT(OUT) :: c

    c = a + b
END SUBROUTINE
""".lower())

print("Input code:", code)
############ Replaced ############
ast = parse_tools.parse(code, lang=lang)
replaced_code, _ = cr.generate_replaced(ast)
print('Replaced code:', replaced_code)

############ Semantical Split ############ 
splitted_tokens = lexicalize(replaced_code, lang=lang, replaced=True)
print('Splitted tokens:', splitted_tokens)

############ Tokenization ############
# Path to vocab
script_dir = os.path.dirname(os.path.realpath(__file__))
tokenizer = Tokompiler(os.path.join(script_dir, "../tokenizer_vocab/vocab.txt"))
ids, attention_mask = tokenizer.encode(splitted_tokens)
print('IDs:', ids)
print('Attention mask:', attention_mask)

decoded_seq = tokenizer.decode(ids)
print('Decoded seq:', decoded_seq)
