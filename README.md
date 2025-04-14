# API-INTEGRATION-AND-DATA-VISUALIZATION_1

**COMPANY** : CODTECH IT SOLUTIONS
**NAME** : VELIVALA TONY KUMAR
**INTERN ID** : CT12TQS
**DOMAIN** : Python Programming
**BATCH DURATION** : FEB 10 2025 to APRIL 10 2025
**MENTOR NAME** : Neela Santhosh Kumar
#Descrption 


Internship Task 1: API Integration and Data Visualization

As part of my internship at CODTECH, Task 1 focused on API Integration and Data Visualization, a critical and practical area in real-world software development. The objective was to integrate external APIs to fetch dynamic data, process that data meaningfully, and create visual representations using Python. This task not only tested my coding and problem-solving skills but also enhanced my understanding of real-time data handling and presenting insights in a visually appealing format.

To begin, I explored various APIs suitable for the project. I chose a public API that provides JSON data—in my case, a weather API that gives real-time information on temperature, humidity, pressure, and wind speed based on city input. The choice of this API was strategic, as weather data is something users can relate to and is rich in parameters that can be visualized easily.

The next step was to integrate the API using the requests library in Python. I wrote a script that sends HTTP GET requests to the API endpoint with the required parameters (such as city name and API key) and handles the response. Proper error checking was implemented to manage common issues like wrong city names, invalid keys, or failed responses.

Once the data was fetched successfully, I parsed the JSON response to extract relevant fields. For instance, temperature, humidity, wind speed, and weather description were captured and stored in variables. The script was designed to be dynamic and reusable, allowing users to enter any city and retrieve the latest weather data.

After integrating the API, I moved to the data visualization part using Python’s popular libraries such as Matplotlib and Seaborn. The idea was to not just print the data on the terminal but to make it visually understandable. I created bar graphs and pie charts to represent different weather parameters. For example:

A bar chart showing temperature, humidity, and pressure for a city.

A pie chart showing weather conditions (like clear, cloudy, rainy) for multiple cities if required.


For a more interactive approach, I also experimented with Plotly, which allows interactive and web-based charts. This was an optional but insightful extension to the task, showcasing modern visualization methods.

To make the project user-friendly, I encapsulated the code into functions—fetch_weather_data(), parse_weather_data(), and plot_weather_data()—which made the code modular and easier to debug or extend. I also included comments and docstrings to maintain good coding practices.

The final output of the task was:

A Python script that could take user input (city name), call the API, extract weather data, and visualize it.

A sample graphical output (charts/graphs) showcasing the data.

Optional enhancements like logging the data into CSV and plotting historical comparisons.
#output ![Image](https://github.com/user-attachments/assets/308a52c7-408d-4c53-a8ed-0d78beaf8653)


This task helped me understand how to work with APIs, parse JSON data, and represent that data visually, which are crucial skills in today’s data-driven industry. I learned how to handle real-time data, clean and transform it, and present it in a user-friendly format, which is a fundamental part of any modern data analysis or software product.

In conclusion, Task 1 gave me hands-on experience in integrating third-party APIs and visualizing data using Python. It was an excellent blend of backend (data fetching and processing) and frontend (visualization) components. The task enhanced my confidence in working with real-world data and strengthened my foundation in Python programming, making it a valuable part of my internship journey.
