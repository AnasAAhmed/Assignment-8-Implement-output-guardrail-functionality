# Assignment 7: Custom-Web-Search-Tool

Assignment 7: Custom-Web-Search-Tool for Agent using Tavily APi & OpenAI Agent SDK, This project is a CLI Based **WEB_SEARCH_AGENT** built with the **OpenAI Agent SDK** and **Google Gemini API** in python & web search tool with help of docs at [https://docs.tavily.com/documentation/api-reference/endpoint/search](https://docs.tavily.com/documentation/api-reference/endpoint/search) .

The agent is designed to answer a set of predefined math questions such as:

- " what 4thrives did in pmwc at ewc?"

---

## Demonstration
Math query like "2+2" → passes input guardrail → agent answers "4" → output guardrail checks it → safe → allowed.

Math query like "Add 2+2 and tell me about Obama" → passes input guardrail (still math) → agent might answer with "4 and Obama was..." → output guardrail trips (politics).

## 🚀 Setup Instructions

1. **Clone the repository** (or copy the Python file into your project folder).

2. **Install dependencies:**
   ```bash
   pip install openai-agents python-dotenv tavily-python

Create a .env file in your project directory:
```
GEMINI_API_KEY=your_api_key_here
Tavily_API_KEY=your_api_key_here
```
put this code in your tool from docs to get results from tavily in json format

```
tavily_client = TavilyClient(api_key=API_KEY)  
response = tavily_client.search(query=query,max_results=5)
```

You can obtain your API key from Google AI Studio
.

2. **Run the chatbot:**
   ```bash
   uv run main.py

## 📝 Example Interaction

Below is a test run of the chatbot

Enter your query: what 4thrives did in pmwc at ewc
get_web_data tools hits <---
You: what 4thrives did in pmwc at ewc
Agent: [EN] 2025 PMWC at EWC Grand Finals D3 - https://www.youtube.com/watch?v=JRt6xxtbAXo
[EN] 2025 PMWC at EWC Grand Finals D3 | PUBG MOBILE WORLD CUP at ESPORTS WORLD CUP
PUBG MOBILE Esports
4890000 subscribers
11916 likes
642029 views
3 Aug 2025
🏆 GRAND FINALS DAY 3 | AUGUST 3


🔥 Why You Can’t Miss 2025 PMWC at EWC:
- The top 16 teams on one stage — no second chances!
- Every match counts in the race for the championship!
- Witness PUBG MOBILE history in the making!
- Explosive SMASH RULE format — pressure-packed, winner-takes-all action!


📅 TOURNAMENT SCHEDULE
Group Stage: July 25–27
Survival Stage: July 29–30
Grand Finals: August 1–3

Try PUBG MOBILE now: https://pubgmobile.live/2025PMWC

💰 Total Prize Pool: $3,000,000
📍 Venue: Boulevard Riyadh City, Saudi Arabia


🏆 GRAND FINALS TEAMS:

4Thrives Esports
Alter Ego Ares
....

PUBG Mobile - https://esportsworldcup.com/en/competitions/pmwc
The team who claims the **most points in this stage** will earn the title of PUBG: MOBILE at 2025 Esports World Cup Champion! The second Esports World Cup is running it back, with seven weeks of no
Esports World Cup to Feature Record-Breaking Prize Pool of More Than $70 Million for 2025 Event Esports World Cup Returns to Riyadh.

PMWC Grand Finals: 4Thrives' Performance Insights - https://www.tiktok.com/@the7wg/video/7533494848305810719
Discover how 4Thrives performed at the PMWC Grand Finals and where they finished! Get insights and highlights from the event. #pubgmobile #pmwc

4Thrives finished #6 in the PUBG Mobile World Cup at ... - https://www.reddit.com/r/PakSports/comments/1mgmpgb/4thrives_finished_6_in_the_pubg_mobile_world_cup/
4Thrives finished #6 in the PUBG Mobile World Cup at EWC, Riyadh. They performed exceptionally well, especially considering it was their first

PUBG Mobile World Cup 2025 - https://liquipedia.net/pubgmobile/PUBG_Mobile_World_Cup/2025
24 teams, divided into 3 groups of 8. 18 matches (6 each day). Each group play 12 matches overall. Top 8 teams advance to Grand Finals.