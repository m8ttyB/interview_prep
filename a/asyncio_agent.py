import aiohttp
import asyncio


async def make_request(session, url):
    async with session.get(url) as resp:
        return await resp.json()


async def run(url, num_threads=10):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_threads):
            tasks.append(asyncio.ensure_future(make_request(session, url)))
        responses = await asyncio.gather(*tasks, return_exceptions=True)

        results = []
        for resp in responses:
            results.append(resp)
        return results


def tabulate_results(results):
    resp_buckets = {
        "Good checkin": 0,
        "Bad request": 0,
        "Server error": 0,
    }
    for result in results:
        resp_buckets[result['Message']] += 1

    return resp_buckets


if __name__ == "__main__":
    url = 'http://127.0.0.1:5001/v1/checkin'
    results = asyncio.get_event_loop().run_until_complete(run(url, 1000))
    counts = tabulate_results(results)
    print(counts)
