# IP-Based Weather and Geolocation App

This application fetches the user's public IP address, determines their geolocation, and provides real-time weather updates for their city. It uses APIs to seamlessly combine IP-based geolocation and weather information into a simple Python program.

---

## Features

- **IP Address Fetching**: Retrieves the user's public IP address.
- **Geolocation Data**: Provides city, country, latitude, and longitude based on the IP address.
- **Weather Information**: Displays current temperature, humidity, and weather conditions.
- **Dynamic Data Integration**: Real-time data fetched using external APIs.

---

## Project Structure

```
IP-Based Weather App/
├── main.py                     # Main application script
├── .env                        # Environment variables file
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Data Collection and Processing

### API Integration
The application integrates with two APIs for its functionality:

1. **IP2Location API**: Provides geolocation details based on the user's IP address.
   - Endpoint: `https://api.ip2location.io/?key={API_KEY}&ip={ip}&format=json`

2. **WeatherAPI**: Fetches weather data for the user's city.
   - Endpoint: `http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}`

---

## Technologies Used

### Backend
- **Python**: Programming language for application logic.
- **Requests**: Library for HTTP requests.
- **dotenv**: Library for loading environment variables from a `.env` file.

### APIs
- **IP2Location API**: For geolocation data.
- **WeatherAPI**: For weather updates.

---

## Getting Started

### Prerequisites
Ensure the following are installed on your system:
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd IP-Based Weather App
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your API keys:
   ```ini
   IP2LOCATION_API_KEY=your_ip2location_api_key
   WEATHER_API_KEY=your_weather_api_key
   ```

5. Run the application:
   ```bash
   python main.py
   ```

---

## Features in Detail

### IP Address Fetching
- Uses `ipify.org` to fetch the user's public IP address.

### Geolocation Data
- Fetches city, country, latitude, and longitude from IP2Location API.

### Weather Information
- Fetches weather conditions, temperature, and humidity from WeatherAPI.

---

## Credits for AI Assistance

This project was developed with assistance from AI tools like ChatGPT. AI contributed to:
- Structuring the code for API integrations.
- Writing helper functions for data fetching.
- Designing error handling and user-friendly responses.

All AI-generated code was reviewed and customized to fit the project requirements.

---

## Contributing

Feel free to contribute to this project. Submit pull requests or open issues for feature suggestions or bug fixes.

---
