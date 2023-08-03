import lmppl 
import pygments 
from pygments.lexers import get_lexer_by_name
import numpy as np 

def get_lex_count(texts,lang,show_lex=True):
	lexer = get_lexer_by_name(lang)
	if show_lex:
		print(f'the count is made with: {lexer}')
	pygments_len=sum(len(list(pygments.lex(t, lexer))) for t in texts)
	lex_vocab = sum(len(v) for v in lexer.tokens.values())
	return pygments_len*lex_vocab

def decoder_only_perplexity(texts,model_path,lex_count:int,batch:int =32):
	scorer=lmppl.LM(model_path)
	raw=np.log(scorer.get_perplexity(texts,batch=batch))
	num_model_tokens=sum(len(x) for x in scorer.tokenizer(texts)['input_ids'])
	scaler=num_model_tokens/lex_count
	return np.exp(np.sum(raw)*scaler)

def encoder_decoder_perplexity(texts,model_path,lex_count:int,batch:int =32):
	scorer=lmppl.EncoderDecoderLM(model_path)
	inputs=['' for _ in texts]
	raw=np.log(scorer.get_perplexity(input_texts=inputs,output_texts=texts,batch=batch))
	num_model_tokens=sum(len(x) for x in scorer.tokenizer(texts)['input_ids'])
	scaler=num_model_tokens/lex_count
	return np.exp(np.sum(raw)*scaler)

if __name__=='__main__':
	texts = [
    'I am happy.',
    'I am sad.  jussst stuff for padddingnngnng dd'
	]
	count=get_lex_count(texts,'c')
	print(decoder_only_perplexity(texts,'gpt2',count))
	print(encoder_decoder_perplexity(texts,'google/flan-t5-small',count))
