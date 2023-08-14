
from tokompiler import convert_representation as cr
from tokompiler import lexicalize
from tokompiler import Tokompiler


lang = 'fortran' 
code = """SUBROUTINE MySubroutine(a, b, c)
    REAL, INTENT(IN) :: a, b
    REAL, INTENT(OUT) :: c

    c = a + b
END SUBROUTINE
"""

############ Replaced ############ 
replaced_code = cr.generate_replaced(code, lang)
print(replaced_code)

############ Semantical Split ############ 
splitted_tokens = lexicalize(replaced_code, lang)
print(splitted_tokens)

############ Tokenization ############
# Path to vocab
tokenizer = Tokompiler('path_to_vocab.txt')
encoded_seq = tokenizer.encode(splitted_tokens)
print(encoded_seq)

decoded_seq = tokenizer.decode(encoded_seq)
print(decoded_seq)
