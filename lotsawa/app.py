import tensorflow as tf
import keras_nlp
import pickle

# load in pickled tokenizers
with open('../tokenizers/eng-tokenizer.pickle', 'rb') as handle:
    eng_tokenizer = pickle.load(handle)

with open('../tokenizers/tib-tokenizer.pickle', 'rb') as handle:
    tib_tokenizer = pickle.load(handle)

# load in model
tib_eng_translator = tf.keras.models.load_model("../models/tib-eng-translator-0.2.0.keras")

# define constants
MAX_SEQUENCE_LENGTH = 15
VOCAB_SIZE = 15000
EMBED_DIM = 256
INTERMEDIATE_DIM = 2048
NUM_HEADS = 8
AUTOTUNE = tf.data.AUTOTUNE

# define translation function
def translate(input_sentences):

    input_sentences = tf.constant([input_sentences])

    batch_size = tf.shape(input_sentences)[0]

    encoder_input_tokens = tib_tokenizer(input_sentences).to_tensor(
        shape=(None, MAX_SEQUENCE_LENGTH)
    )

    def next(prompt, cache, index):
        logits = tib_eng_translator([encoder_input_tokens, prompt])[:, index - 1, :]
        hidden_states = None
        return logits, hidden_states, cache
    
    length = MAX_SEQUENCE_LENGTH
    start = tf.fill((batch_size, 1), eng_tokenizer.token_to_id("[START]"))
    pad = tf.fill((batch_size, length - 1), eng_tokenizer.token_to_id("[PAD]"))
    prompt = tf.concat((start, pad), axis=-1)

    generated_tokens = keras_nlp.samplers.GreedySampler()(
        next,
        prompt,
        end_token_id=eng_tokenizer.token_to_id("[END]"),
        index=1
    )
    generated_sentences = eng_tokenizer.detokenize(generated_tokens)
    try:
        generated_sentences = generated_sentences.numpy()[0].decode("utf-8")

        generated_sentences = (
            generated_sentences.replace("[PAD]", "")
            .replace("[START]", "")
            .replace("[END]", "")
            .replace("[UNK]", "")
            .strip()
        )
    except:
        pass
    return generated_sentences

def main():
    # TODO
    pass