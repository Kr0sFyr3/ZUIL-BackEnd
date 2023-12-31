import json

import requests


class API:
    def __init__(self):
        self.base_url = "https://hub.adainforma.tk/api/v1"
        self.header = {'Accept': 'application/json'}
        self.token = None

    def login(self, email, password):
        login_url = f"{self.base_url}/login"
        data = {'email': email, 'password': password}

        try:
            response = requests.post(login_url, headers=self.header, data=data)

            authorisation = response.json().get('authorisation')
            self.token = authorisation.get('token')
            token_type = authorisation.get('type')

            if response.status_code == 200:
                # Print the authentication token or handle it as needed
                print(f"Login successful. Authentication Token: {self.token}")
                self.header.update({'Authorization': f"Bearer {self.token}"})
            else:
                # Print an error message if the login was unsuccessful
                print("Login failed. Status Code:", response.status_code, "Message:", response.text)

        except requests.exceptions.RequestException as e:
            # Handle exceptions, such as network errors
            print("Error:", e)

    def get_students(self):
        students_url = f"{self.base_url}/student"

        try:
            response = requests.post(students_url, headers=self.header)

            students = json.dumps(response.json(), indent=4)
            return students
        except requests.exceptions.RequestException as e:
            print("Error", e)

    def get_student_by_id(self, student_id):
        student_url = f"{self.base_url}/student/{student_id}"

        try:
            response = requests.post(student_url, headers=self.header)

            student = json.dumps(response.json(), indent=4)
            return student
        except requests.exceptions.RequestException as e:
            print("Error", e)

    def get_tags(self):
        tags_url = f"{self.base_url}/tag"

        try:
            response = requests.post(tags_url, headers=self.header)

            tags = json.dumps(response.json(), indent=4)
            return tags
        except requests.exceptions.RequestException as e:
            print("Error", e)

    def get_student_by_tag_id(self, tag_id):
        tag_id_url = f"{self.base_url}/tag/{tag_id}"

        try:
            response = requests.post(tag_id_url, headers=self.header)

            data = response.json()
            tag = data.get("data", [])[0]
            student_id = tag.get("student", None)
            student = self.get_student_by_id(student_id)
            return student
        except requests.exceptions.RequestException as e:
            print("Error", e)
