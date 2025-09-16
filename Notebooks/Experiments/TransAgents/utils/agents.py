import abc
import ollama
import datetime

class Agent(abc.ABC):
    def __init__(self):
        self.sys_message = {'role': 'system', 'content': self.system_prompt()}
        self.user_message_default = "Introduce yourself."
        self.report = {}

    @abc.abstractmethod
    def system_prompt(self):
        """Return the system prompt content"""
        pass
    
    @abc.abstractmethod
    def user_prompt(self):
        pass

    def generate_report(self, user_message, response):

        self.report['time_created'] = datetime.datetime.now()
        self.report['duration'] = f'{round(response['total_duration'] / 60_000_000_000, 3)} mins'

        self.report['input'] = user_message
        self.report['output'] = response['message']['content'].strip()


    def chat(self, user_input=None, model="gemma3n"):

        if user_input:
            user_content = self.user_prompt(user_input)
        else:
            user_content = self.user_message_default

        user_message = {'role': 'user', 'content': user_content}

        response = ollama.chat(model=model, messages=[self.sys_message, user_message])

        self.generate_report(user_message=user_message, response=response)        

        return response['message']['content'].strip()
    
class Preprocessor(Agent):
    def system_prompt(self):
        return "You are an expert editor of Tibetan Buddhist texts. You preprocess Tibetan material for translation."
    
    def user_prompt(self, user_input):
        return f"""Preprocess the following: {user_input}
                """
    
class Translator(Agent):
    def system_prompt(self):
        return "You are an expert translator of Tibetan Buddhist texts. You translate clearly and concisely, preserving the original intent of the text."
    
    def user_prompt(self, user_input):
        return f"""Translate the following from Tibetan to English:{user_input['source']}
                Consider these notes from the preprocessor: {user_input['prepro_notes']}"""
    
class Evaluator(Agent):
    def system_prompt(self):
        return "You are an expert in translation evaluation. You score translations based on fluency, literary quality, and meaning preservation."
    
    def user_prompt(self, user_input):
        return f"""Score the following translation on a continuous scale from 0 to 100, where score of zero means
                "no meaning preserved" and score of one hundred means "perfect meaning and grammar".

                Source: {user_input['source']}
                Target: {user_input['target']}
                """
    
class PostEditor(Agent):
    def system_prompt(self):
        return """"You are an expert translation editor. You provide improved translations based on an original translation and a score from an evaluator. 
        You preserve the good qualities of the first draft but improve clarity and fluency."""
    
    def user_prompt(self, user_input):
        return f"""Improve the following translation:
        Source: {user_input['source']},
        Translation: {user_input['translation']}
        Evaluation: {user_input['evaluation']}
        """
    
class FinalEditor(Agent):
    def system_prompt(self):
        return """"You are an expert editor. You provide final drafts of translations based on the work of translators. 
        You take into account their input and provide the final translation, with no additional outputs."""
    
    def user_prompt(self, user_input):
        return f"""Provide a final draft output based on this draft and information from the translation team: {user_input}
        """
    
class Team():

    def __init__(self):

        self.preprocessor = Preprocessor()
        self.translator = Translator()
        self.evaluator = Evaluator()
        self.post_editor = PostEditor()
        self.final_editor = FinalEditor()

        self.roster = [self.preprocessor, self.translator, self.evaluator, self.post_editor, self.final_editor]

        self.report = {}

    def translate(self, user_input):

        prepro_notes = self.preprocessor.chat(user_input=user_input)
        prelim_trans = self.translator.chat({'source':user_input, 'prepro_notes':prepro_notes})
        evaluation = self.evaluator.chat({'source': user_input, 'target': prelim_trans})
        post = self.post_editor.chat({'source': user_input, 'translation': prelim_trans, 'evaluation':evaluation})
        final = self.final_editor.chat(post)

        self.generate_report()

        return final


    def generate_report(self):
        
        for agent in self.roster:
            self.report[type(agent).__name__] = agent.report

        