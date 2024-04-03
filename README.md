# Pixela API Project

This project demonstrates how to use the Pixela API to create and manage graphs for tracking personal data.

## About Pixela

Pixela is a habit tracking API that allows users to create graphs and track various activities or habits over time.

You can find more information about Pixela [here](https://pixe.la/).

## Getting Started

1. Sign up for an account on Pixela.
2. Obtain your API token from your account settings.
3. Update the `USERNAME`, `TOKEN`, and `ID` variables in the script with your Pixela username, API token, and desired graph ID.
4. Run the Python script `main.py` to interact with the Pixela API.

## Features

- **Creating a User**: Create a user on Pixela using your username and API token.
- **Creating a Graph**: Define a new graph to track specific data, such as study time, exercise duration, or any custom metric.
- **Posting Data**: Post data points to your graph to track your progress over time. For example, input how many minutes you studied today.
- **Updating Data**: Update existing data points on your graph.
- **Deleting Data**: Delete specific data points from your graph.

## Files

- `main.py`: Contains the main script to interact with the Pixela API. It includes functionalities to create users, graphs, post data, update data, and delete data.
- `requirements.txt`: Lists the Python dependencies required for running the script.

## Dependencies

- Python 3.x
- Requests library (install via `pip install requests`)

## Configuration

Ensure you have the following variables correctly set in the `main.py` script:

- `USERNAME`: Your Pixela username.
- `TOKEN`: Your Pixela API token.
- `ID`: The unique ID for your graph.

## Usage

1. Run the Python script `main.py`.
2. Follow the prompts to create a user, graph, post data, update data, or delete data.
