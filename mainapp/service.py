import requests 

def get_all_characters():
    """
    Retrieves all characters from the Rick and Morty API and returns them as a list of dictionaries.

    This function makes multiple requests to the Rick and Morty API to fetch all available characters.
    It handles pagination and combines the results into a single list.

    Returns:
    list: A list of dictionaries, where each dictionary contains information about a single character.
          The dictionary keys are 'id', 'name', 'status', 'species', 'type', 'gender', 'origin', and 'location'.

    Raises:
    requests.RequestException: If there's an error with the HTTP request.
    ValueError: If the API response is not in the expected format.

    Note:
    This function requires the 'requests' library to be installed.
    """
    base_url = "https://rickandmortyapi.com/api/character"
    all_characters = []

    while base_url:
        response = requests.get(base_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        print(data)
    

        if not isinstance(data, dict) or 'results' not in data:
            raise ValueError("Unexpected API response format")

        all_characters.extend(data['results'])

        # Check if there are more pages
        base_url = data.get('info', {}).get('next')
    return all_characters


def get_character_by_page(page=0):
    base_url = f"https://rickandmortyapi.com/api/character/?page={page}"
    response = requests.get(base_url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    data = response.json()

    if 'error' in data:
        return 
    return data

def get_character_by_id(id):
    base_url = f"https://rickandmortyapi.com/api/character/{id}"
    response = requests.get(base_url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    data = response.json()

    if 'error' in data:
        return
    return data