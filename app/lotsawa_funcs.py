import os
# silence TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import keras_nlp

# define constants
MAX_SEQUENCE_LENGTH = 15
VOCAB_SIZE = 15000
EMBED_DIM = 256
INTERMEDIATE_DIM = 2048
NUM_HEADS = 8
AUTOTUNE = tf.data.AUTOTUNE

### HELPER FUNCTION

# define function for progress bar
def progress_bar(i, total):
    length = 30
    progress = int(round((i / total) * length, 0))
    filled = ('=' * (progress-1)) + '>'
    not_filled = '_' * (length - progress)
    bar = '[' + filled + not_filled + ']'
    return bar

# define function to write logs
def write_logs(info, window):
    try:
        with open('outputs/logs.txt', 'w') as output:
            output.writelines('\n'.join(str(log).replace('(', '').replace(')', ''). replace('\'', '').replace(',', ' at ') for log in info))
        info.append('Process logs were saved to \'logs.txt\'')
        window["-MONITOR-"].update('\n'.join(info))
        window.refresh()
    except:
        info.append('Logs Were Not Saved Correctly')
        window["-MONITOR-"].update('\n'.join(info))
        window.refresh()


### MAIN FUNCTIONS

# define translation function
def translate_line(input_sentences, eng_tokenizer, tib_tokenizer, tib_eng_translator):

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

    generated_tokens = keras_nlp.samplers.TopKSampler(4)(
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

def translate_text(in_text, eng_tokenizer, tib_tokenizer,tib_eng_translator, window, info):
    # initialize counter of translated lines and flag for successful opening of input
    i = 1

    translation = []

    # translated inputted file
    with open(in_text, 'r') as file:

        # get number of lines to be translated
        contents = file.readlines()
        total = len(contents)

        for line in contents:
            # show progress bar
            window['-MONITOR-'].update('\n'.join(info) + '\n' + progress_bar(i, total))
            window.refresh()

            # translate line
            translated_line = translate_line(line, eng_tokenizer, tib_tokenizer,tib_eng_translator)
            translation.append(line.replace('\n', ''))
            translation.append(translated_line)
            translation.append('\n')
            i += 1

        return '\n'.join(translation)
