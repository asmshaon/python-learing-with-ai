import asyncio


# Coroutine function
async def fetch_web_data(source_id):
    print(f"Starting fetch for source {source_id}...")
    # Yields control back to the event loop for 2 seconds
    await asyncio.sleep(2)
    print(f"Finished fetch for source {source_id}!")
    return {"id": source_id, "data": "success"}


# Main Coroutine
async def main():
    # Runs both tasks concurrently without blocking each other
    task1 = fetch_web_data(1)
    task2 = fetch_web_data(2)

    results = await asyncio.gather(task1, task2)
    print(results)


# Starting the main routine event loop
asyncio.run(main())
