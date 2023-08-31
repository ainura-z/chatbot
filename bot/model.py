import torch
from transformers import AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained('tinkoff-ai/ruDialoGPT-medium')
model = torch.load('D:/studies/masters/innopolis/study/internships/Tinkoff/bot/model', map_location=torch.device('cpu'))
chat_history_ids = [[]]

def get_response(text, step):
    global chat_history_ids
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(f'@@ПЕРВЫЙ@@ {text} @@ВТОРОЙ@@', return_tensors='pt')
    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
    # generated a response while limiting the total chat history to 1000 tokens,
    chat_history_ids = model.generate(
                                        bot_input_ids,
                                        top_k=10,
                                        top_p=0.95,
                                        num_beams=3,
                                        num_return_sequences=1,
                                        do_sample=True,
                                        no_repeat_ngram_size=2,
                                        temperature=1.2,
                                        repetition_penalty=1.2,
                                        length_penalty=1.0,
                                        pad_token_id=tokenizer.eos_token_id,
                                        max_new_tokens=30
                                     ) 
    # pretty print last ouput tokens from bot
    respond = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    return respond
