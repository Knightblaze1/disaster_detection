Table of Contents

    Overview

    Features

    Installation

    Usage

    Deployment

    Contributing

    License

    Acknowledgments


Overview

This project is an open-source AI framework designed to detect natural disasters (floods, tsunamis, tornadoes, wildfires, earthquakes) and provide early warnings to communities. It integrates real-time data from open APIs, uses machine learning models for prediction, and provides a user-friendly dashboard for visualization and alerts. The system also links disasters to CO₂ emissions to advocate for climate justice.

Features

    Real-Time Disaster Detection:
    Floods, tsunamis, tornadoes, wildfires, and earthquakes.

    Early Warning System:
    SMS alerts via Twilio.

    Interactive Dashboard:
    Real-time maps and visualizations using Streamlit and Folium.

    Multilingual Support:
    Translate alerts and dashboard text using Google Translate API.

    Community Engagement:
    Allow users to report disasters and contribute data.

    Climate Justice:
    Link disasters to CO₂ emissions for advocacy.
    
Installation
Prerequisites

    Python 3.8 or higher

    pip (Python package manager)Steps

    Clone the repository:
    git clone https://github.com/Knightblaze1/disaster_detection.git
    cd disaster_detection
    pip install -r requirements.txt
    pip install streamlit pandas numpy requests scikit-learn tensorflow twilio
    
    
Usage
Running Locally
    Start the Streamlit app: 
    streamlit run disaster_detection.pyUsing the Dashboard

Disaster Detection:
	View real-time data for floods, tsunamis, tornadoes, wildfires, and 
	earthquakes.
Alerts:
	Enter your phone number to receive SMS alerts.
ommunity Reports:
	submit disaster reports and view community-contributed data.
Multilingual Support:
	Select your preferred language from the sidebar.
	
	

Deployment Heroku
	Install the Heroku CLI: Heroku CLI.
	Create a Procfile:
	web: streamlit run --server.port $PORT disaster_detection.py
Deploy:
	heroku login
	heroku create your-app-name
	git init
	git add .
	git commit -m "Initial commit"
	git push heroku master

AWS/GCP
Create a Dockerfile:
	FROM python:3.9-slim
	WORKDIR /app
	COPY . .
	RUN pip install -r requirements.txt
	CMD streamlit run disaster_detection.py --server.port 8501 --server.address 
	0.0.0.0
	
Contributing
We welcome contributions! Here’s how you can help:
	Report Bugs: Open an issue on GitHub.
	Suggest Features: Share your ideas in the discussions section.

Submit Pull Requests:
	Fork the repository.
        Create a new branch (git checkout -b feature/YourFeature).
        Commit your changes (git commit -m 'Add some feature').
        Push to the branch (git push origin feature/YourFeature).
        Open a pull request.
        
License
	This project is licensed under the MIT License. See the LICENSE file for 
	details.

Acknowledgments
Data Providers:
	NASA FIRMS, NOAA, USGS, Climate TRACE, Global Forest Watch.
   
Libraries:
        Streamlit, TensorFlow, Scikit-learn, Folium, Twilio.

Community:
	OpenStreetMap, Ushahidi, and all contributors.
	
Contact
For questions or feedback, please contact:
Your Name
    Email: knightblaze.ai@gmail.com
    GitHub: knightblaze1
    



   

    
    
    
    
    
    
