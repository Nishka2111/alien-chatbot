import random
import re


class AlienBot:

    def __init__(self):
        self.name = None

        self.negative_responses = ("no", "nope", "nah", "not really")

        self.exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

        self.random_questions = [
            "Why are you here?\n> ",
            "What do you consume for sustenance?\n> ",
            "Is there intelligent life on this planet?\n> ",
            "Does Earth have a leader?\n> "
        ]

        self.alienbabble = {
            'describe_planet_intent': r'.*\b(planet)\b.*',
            'answer_why_intent': r'.*\bwhy\b.*',
            'cubed_intent': r'.*cube.*number (\d+).*'
        }

    # Greeting the user
    def greet(self):
        self.name = input("Hello there, what's your name?\n> ")

        will_help = input(
            f"Hi {self.name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet?\n> "
        ).lower()

        if will_help in self.negative_responses:
            print("Ok, have a nice Earth day!")
            return

        self.chat()

    # Conversation loop
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()

        while not self.make_exit(reply):
            reply = input(self.match_reply(reply)).lower()

    # Exit condition
    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Ok, have a nice Earth day!")
                return True
        return False

    # Matching user intent
    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.search(regex_pattern, reply)

            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()

            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()

            elif found_match and intent == 'cubed_intent':
                return self.cubed_intent(found_match.group(1))

        else:
            return self.no_match_intent()

    # Intent responses
    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms and species. ",
            "I am from Opidipus, the capital of the Wayward Galaxies. "
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in peace. ",
            "I am here to collect data on your planet and its inhabitants. ",
            "I heard the coffee is good. "
        )
        return random.choice(responses)

    def cubed_intent(self, number):
        number = int(number)
        cubed_number = number * number * number
        return f"The cube of {number} is {cubed_number}. Isn't that cool?"

    def no_match_intent(self):
        responses = (
            "Please tell me more. ",
            "Tell me more! ",
            "Why do you say that? ",
            "I see. Can you elaborate? ",
            "Interesting. Can you tell me more? ",
            "I see. How do you think? ",
            "Why? ",
            "How do you think I feel when you say that? "
        )
        return random.choice(responses)


# Run the chatbot
AlienBot_instance = AlienBot()
AlienBot_instance.greet()