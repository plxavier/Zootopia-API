# Zootopia-API

**A python application using API to fetch data and generate webpage of animals.** 

**Features:**
1. Animal Search: Find scientific information about any animal
2. API Integration: Real-time data from Animals Ninja API
3. HTML Generation: Creates animal profile pages
4. Data Persistence: Saves animal data of the latest search to JSON for offline use


**Quick Start**
```bash
git clone https://github.com/plxavier/Zootopia-API.git
cd Zootopia-API
```
**Install Dependencies**
```bash
pip install -r requirements.txt
```

**API**
- Sign up at API-Ninja for API Key
- Set up the environment in .env file with the API key

**Run the Application**
```bash
python animals_web_generator.py
Enter the animal name:
```
-Open the generated animals.html in your favourite web-browser

**File Structure**
```bash
Zootopia-API/
├── data_fetcher.py          # Main data fetching module
├── animals_web_generator.py  # HTML generation module  
├── animals_template.html    # HTML template
├── .env                     # API configuration
├── animals_data.json        # Auto-generated data storage
└── animals.html            # Auto-generated webpage
```

**Contributing**
-Do fork via GitHub
```bash
git checkout -b feature/xx
```
- Then add, commit, push, and pull request, wait for review to get your contributions accepted!
Thanks!

