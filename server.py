import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/trueway/api/trueway-matrix'

mcp = FastMCP('trueway-matrix')

@mcp.tool()
def calculate_driving_distance_matrix(origins: Annotated[str, Field(description='List of origins described as semicolon-delimited coordinate pairs with latitudes and longitudes. Max: 25')],
                                      start_time: Annotated[Union[str, None], Field(description='Time when travel is expected to start. You can specify the time as an integer in seconds since midnight, January 1, 1970 UTC or you can use "now" to specify the current time.')] = None,
                                      destinations: Annotated[Union[str, None], Field(description='List of destinations described as semicolon-delimited coordinate pairs with latitudes and longitudes. If not specified, an n x n matrix will be generated using the origins. Max: 25')] = None,
                                      avoid_highways: Annotated[Union[bool, None], Field(description='avoid highways')] = None,
                                      avoid_tolls: Annotated[Union[bool, None], Field(description='avoid toll roads')] = None,
                                      avoid_ferries: Annotated[Union[bool, None], Field(description='avoid ferries')] = None) -> dict: 
    '''Calculate distances and durations between a set of origins and destinations.'''
    url = 'https://trueway-matrix.p.rapidapi.com/CalculateDrivingMatrix'
    headers = {'x-rapidapi-host': 'trueway-matrix.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'origins': origins,
        'start_time': start_time,
        'destinations': destinations,
        'avoid_highways': avoid_highways,
        'avoid_tolls': avoid_tolls,
        'avoid_ferries': avoid_ferries,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
