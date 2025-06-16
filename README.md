markdown
# TrueWay Matrix MCP Server

## Overview

TrueWay Matrix is a powerful tool designed to provide precise durations (in seconds) and distances (in meters) between a set of origins and destinations. Leveraging the routes calculated by the TrueWay Directions tool, it offers accurate estimations based on either predictive or live traffic data, depending on the start time specified in the request.

This tool is essential for a variety of applications, including:

- Solving the Traveling Salesman Problem (TSP).
- Addressing the Vehicle Routing Problem (VRP).
- Sorting search results by actual travel distance or time.
- Determining arrival times based on travel times.
- Calculating commute time differences between locations.
- Clustering data based on travel time and distances.

## Key Features

- **Global Road Network Coverage:** Access a comprehensive network for accurate distance and duration calculations.
- **Traffic-Based Calculations:** Optionally calculate traffic-influenced distance/duration matrices over specified timeframes.
- **Route Preferences:** Ability to avoid toll roads, highways, or ferries as per user requirements.

## Tool Description

### Calculate Driving Distance Matrix

The primary function of the TrueWay Matrix tool is the `CalculateDrivingDistanceMatrix`. This function takes a list of origin and destination locations and returns a matrix of distances and durations between them. The output provides the optimal route length and travel time between each pair of origin and destination points on the real road network.

**Required Parameters:**

- **`origins`**: A list of origins described as semicolon-delimited coordinate pairs with latitudes and longitudes. Maximum of 25 origins per request.

**Optional Parameters:**

- **`destinations`**: A list of destinations described similarly to origins. If not specified, an n x n matrix will be generated using the origins. Maximum of 25 destinations per request.
- **`start_time`**: The expected start time of travel. Can be specified as an integer in seconds since the Unix epoch or as "now" for the current time. Must be current or future time.
- **`avoid_highways`**: Option to avoid highways.
- **`avoid_tolls`**: Option to avoid toll roads.
- **`avoid_ferries`**: Option to avoid ferries.

## Response Structure

The response from the `CalculateDrivingDistanceMatrix` tool includes:

- **Distances**: A two-dimensional array representing distances from origins to destinations.
- **Durations**: A two-dimensional array representing driving times (durations) from origins to destinations.

This tool is ideal for developers and businesses looking to integrate sophisticated routing and travel time analytics into their applications.