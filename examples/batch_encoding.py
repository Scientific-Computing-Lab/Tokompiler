import os

from tokompiler import parse_tools, convert_representation as cr
# from ast.tokenizer import Tokompiler
from tokompiler import lexicalize, Tokompiler

code = """FUNCTION calculate_pi(max, seed) RESULT(pi)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: max, seed
  REAL(8) :: pi
  REAL(8) :: area, x, y
  INTEGER :: i
  EXTERNAL :: DRAND48

  INTEGER :: pi_count

  pi_count = 0
  CALL seed48(seed)

  DO i = 1, max
     x = DRAND48() * 2 - 1
     y = DRAND48() * 2 - 1
     IF (x * x + y * y < 1) THEN
        pi_count = pi_count + 1
     END IF
     area = 4.0 * REAL(pi_count) / REAL(i)
  END DO

  pi = 4.0 * REAL(pi_count) / REAL(max)
END FUNCTION
""".lower()

ast = parse_tools.parse(code, lang='fortran')
replaced_code, _ = cr.generate_replaced(ast)

lex = lexicalize(replaced_code, lang='fortran', replaced=True)

script_dir = os.path.dirname(os.path.realpath(__file__))
tokenizer = Tokompiler(vocab_path=os.path.join(script_dir, "../tokenizer_vocab/vocab.txt"))

tokenizer.enable_padding(length=256)
# encodigs = tokenizer.encode_batch([lex])

# print(encodigs.ids)
encodings, attention_mask = tokenizer.encode(lex)

print(encodings)
print(attention_mask)

encodings[-1] = tokenizer.mask

print(tokenizer.decode_batch([encodings], skip_special_tokens=False))