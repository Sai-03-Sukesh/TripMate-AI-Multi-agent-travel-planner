# from tools.tavily_tool import tavily_search

# results = tavily_search("Give me budget hotels in Shiridi")
# print(results)

# from tools.flight_tool import search_flights
# print(search_flights("Plan a 7 days Japan trip from Bangladesh"))

from backend import run_travel_agent
response = run_travel_agent(
    user_input = "Plan a 7 days Bali trip from India including flights, hotels and sightseeing under 2 lakhs",
    thread_id = "test_user"
)
print(response)