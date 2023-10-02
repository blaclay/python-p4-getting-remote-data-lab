import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(self.url)
        return response.content

    def load_json(self):
        programs_list = []
        programs = json.loads(self.get_response_body())
        for program in programs:
            programs_list.append(program)

        return programs_list

programs = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
requested = programs.get_response_body()
print(requested)
program_list = programs.load_json()
print(program_list)