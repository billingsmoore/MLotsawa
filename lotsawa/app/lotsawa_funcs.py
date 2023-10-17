import os
# silence TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import keras_nlp
import pickle
import datetime
import sys

# define constants
MAX_SEQUENCE_LENGTH = 15
VOCAB_SIZE = 15000
EMBED_DIM = 256
INTERMEDIATE_DIM = 2048
NUM_HEADS = 8
AUTOTUNE = tf.data.AUTOTUNE

# initialize logs
logs = []

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

# define function for progress bar
def progress_bar(i, total):
    print('Translating document...')
    # clear previous progress
    os.system('clear')
    for line in logs:    
        print(line[0])
    # progress bar
    length = 50
    progress = int(round((i / total) * length, 0))
    filled = '█' * progress
    not_filled = '-' * (length - progress)
    bar = '[' + filled + not_filled + ']'
    return bar

# defining function to keep logs
def log(update):
    print(update)
    logs.append((update, datetime.datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
    return update

# define function to write logs
def write_logs(logs):
    with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/outputs/logs.txt', 'w') as output:
        output.writelines('\n'.join(str(log).replace('(', '').replace(')', ''). replace('\'', '').replace(',', ' at ') for log in logs))
        print('See logs.txt for process information')

def error(problem):
    log(problem)
    write_logs(logs)
    sys.exit()

def load_models():
    # load tokenizers
    try:
        # load in pickled tokenizers
        log('Loading tokenizers...')

        with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/tokenizers/eng-tokenizer.pickle', 'rb') as handle:
            eng_tokenizer = pickle.load(handle)

        with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/tokenizers/tib-tokenizer.pickle', 'rb') as handle:
            tib_tokenizer = pickle.load(handle)

        log('Tokenizers loaded!')
    except:
        error('Tokenizers failed to load')

    # load translation model
    try:
        log('Loading model...')
        tib_eng_translator = tf.keras.models.load_model("/home/j/Documents/Projects/Iron-Bridge/lotsawa/models/tib-eng-translator-0.2.0.keras")
        log('Model loaded!')
    except:
        error('Model failed to load')

    return eng_tokenizer, tib_tokenizer,tib_eng_translator

def save_translation(translation):
    try:
        # write translation to output file
        with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/outputs/output.txt', 'w') as output:
            log('Saving translation...')
            output.writelines('\n'.join(translation))
            log('Translation saved!')

        log('Done!')

    except:
        error('Translation could not be saved')

def translate_text(in_text, eng_tokenizer, tib_tokenizer,tib_eng_translator):
    # initialize counter of translated lines and flag for successful opening of input
    i = 1
    input_opened = False

    try:
        translation = []

        # translated inputted file
        with open(in_text, 'r') as file:
            input_opened = True

            log('Translating document...')

            # get number of lines to be translated
            contents = file.readlines()
            total = len(contents)

            for line in contents:
                # show progress bar
                print(progress_bar(i, total))

                # translate line
                translated_line = translate_line(line, eng_tokenizer, tib_tokenizer,tib_eng_translator)
                translation.append(translated_line)

                i += 1

            log('Document translated!')

            return translation

    except:
        problem = 'Document could not be translated'
        if input_opened == False:
            problem = problem + '\n' + 'Input document could not be opened'
        problem = problem + '\n' + str(i - 1) + ' lines translated'
        error(problem)

def translate(text):
    eng_tokenizer, tib_tokenizer,tib_eng_translator = load_models()
    print('Here 1')
    translation = translate_text(text, eng_tokenizer, tib_tokenizer,tib_eng_translator)
    print('Here!')
    save_translation(translation)
    write_logs(logs)
    return '\n'.join(translation)