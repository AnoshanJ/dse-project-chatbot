from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSendToLlm(Action):
    """Send Query to LLM"""
    def name(self):
        return "action_send_to_llm"

    async def run(self, dispatcher, tracker, domain):
        # Simulate the action's functionality
        print("CAME IN TO THE FUNCTION")
        response = "ASK LLM TEST"
        dispatcher.utter_message(text=response)
        return []

if __name__ == "__main__":
    action = ActionSendToLlm()

    # Create a minimal tracker context for testing
    sender_id = "test_sender_id"
    latest_message = {"text": "Test message"}
    latest_event_time = "2023-11-01T12:00:00.000Z"
    slots = {}
    latest_input_channel = "test"
    active_loop = {}
    latest_action_name = "action_listen"

    # Create a Tracker instance
    tracker = Tracker(
        sender_id,
        slots,
        latest_action_name,
        latest_message,
        latest_event_time,
        latest_input_channel,
        active_loop,
        []
    )

    dispatcher = CollectingDispatcher()

    # Call the run method of the action
    action.run(dispatcher, tracker, {})
