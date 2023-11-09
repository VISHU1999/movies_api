import asyncio

import aiohttp
import requests


async def fetch_data(url, params=None):
    """Calling API in bulk"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                print(f"Failed to fetch data from {url}")
                return None


def get_url_response(url, params=None):
    """Return url response"""
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Return the JSON response or other content as needed
        return response.json()

    # Raise an exception for non-successful status codes
    response.raise_for_status()


async def exact_people_data(people):
    """Return actor data"""
    actor_data = []
    tasks = [
        fetch_data(url, params={"fields": "name,age,species,id"}) for url in people
    ]
    results = await asyncio.gather(*tasks)
    for res in results:
        actor_data.append(res)

    return actor_data


def exact_response_data(response_data):
    """Return list after replacing people data with actor"""
    output = []
    for response in response_data:
        item = asyncio.run(exact_people_data(response["people"]))
        response["actor"] = item
        del response["people"]
        output.append(response)

    return output
