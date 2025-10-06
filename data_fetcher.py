import requests
import os
import json
from typing import Dict, Optional, List
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
HEADERS = {"X-Api-Key": API_KEY}
REQUEST_URL = f"https://api.api-ninjas.com/v1/animals"


def setup_fetcher():
    """Initialize the data fetcher"""
    load_dotenv()
    if not API_KEY:
        print("API_KEY not found in .env file")
        return False
    return True


def fetch_data(animal_name: str) -> Optional[List[Dict]]:
    """
    Search for animal and store ALL results in temporary container
    """
    try:
        params = {"name": animal_name}
        response = requests.get(REQUEST_URL, headers=HEADERS, params=params, timeout=10)

        response.raise_for_status()
        data = response.json()

        if data and len(data) > 0:

            print(f"Found {len(data)} animals matching '{animal_name}'")

            for i, animal in enumerate(data, 1):
                print(f"   {i}. {animal.get('name', 'Unknown')}")
            return data

        else:
            print(f"No animals found matching '{animal_name}'")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {animal_name}: {e}")
        return None


def save_animals_to_file(animals_data, filename: str = "animals_data.json") -> str:
    """Save ALL current animals to JSON file"""

    if not animals_data:
        print("❌ No animal data to save")
        return ""

    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    #Save the list directly (no need to wrap in another list)
    with open(filename, 'w') as f:
        json.dump(animals_data, f, indent=2)
    return filename


def main():
    """Main function to search animal and save data"""
    if not setup_fetcher():
        return None

    animal_name = input("Enter animal name: ").strip()

    animals_data = fetch_data(animal_name)

    if animals_data:
        # Save ALL animals to file
        filename = save_animals_to_file(animals_data)
        print(f"Data for {len(animals_data)} animals with search-term {animal_name} saved to {filename}")
        return animals_data
    else:
        print(f" Could not find data for {animal_name}")
        return None


if __name__ == "__main__":
    main()