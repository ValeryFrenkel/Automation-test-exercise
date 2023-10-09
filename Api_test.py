import requests
import unittest

class PetStoreAPITest(unittest.TestCase):
    base_url = "https://petstore.swagger.io/v2"

    def test_find_pets_by_status_available(self):
        # Define the endpoint and parameters
        endpoint = "/pet/findPetsByStatus"
        params = {"status": "available"}

        # Send a GET request to the endpoint
        response = requests.get(self.base_url + endpoint, params=params)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check that the response contains pets with the "available" status
        pets = response.json()
        for pet in pets:
            self.assertIn("available", pet["status"].lower())

if __name__ == "__main__":
    unittest.main()
