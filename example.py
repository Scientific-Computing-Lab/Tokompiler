import convert_representation as cr
from lexicalization import lexicalize
from tokenizer import Tokompiler


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
tokenizer = Tokompiler('/home/1010/talkad/Tokompiler/tokenizer_vocab/vocab.txt')
encoded_seq = tokenizer.encode(splitted_tokens)
print(encoded_seq)

decoded_seq = tokenizer.decode(encoded_seq)
print(decoded_seq)