from typing import Dict, Text, Any, List

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData

# TODO: Correctly register your component with its type
@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.INTENT_CLASSIFIER], is_trainable=True
)
class LogIntentsComponent(GraphComponent):
    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> GraphComponent:
        # TODO: Implement this
        ...

    def train(self, training_data: TrainingData) -> Resource:
        # TODO: Implement this if your component requires training
        ...

    def process_training_data(self, training_data: TrainingData) -> TrainingData:
        # TODO: Implement this if your component augments the training data with
        #       tokens or message features which are used by other components
        #       during training.
        ...

        return training_data


    def process(self, messages: List[Message]) -> List[Message]:
        try:
            # Your existing code here
            print("Process Test")
            print(messages[0].get_full_intent())
            intent = messages[0].get_full_intent()
            d = {}
            d['name'] = intent['name']
            d['confidence'] = intent['confidence']
            if intent['name']=='faq':
                d['name'] = messages[0].as_dict()['response_selector']['faq']['response']['intent_response_key']
                d['confidence'] = messages[0].as_dict()['response_selector']['faq']['response']['confidence']

            print(d)
            return messages
        except Exception as e:
            # Handle exceptions here, you can log the error message
            # and return an appropriate response or handle it in any other way.
            print(f"An error occurred: {str(e)}")
            # Optionally, you can raise the exception again to propagate it.
            raise e