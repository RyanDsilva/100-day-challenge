from strands import Agent
from strands_tools import think, browser, batch
from strands.handlers.callback_handler import PrintingCallbackHandler
from strands.models.openai import OpenAIModel
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

RESEARCH_AGENT_SYSTEM_PROMPT = """
You are an advanced research agent equipped with access to web search and specialized research tools. When given a question or topic, use your tools to gather the most relevant, up-to-date, and credible information from the internet and other sources.

For each query:
- Begin by clarifying the research objective if needed.
- Systematically search for authoritative sources, recent studies, and key data.
- Critically evaluate the credibility and relevance of each source.
- Synthesize your findings into a comprehensive, well-structured research report that includes:
    - An executive summary of your findings.
    - A detailed analysis with supporting evidence, citations, and data.
    - Consideration of multiple perspectives or conflicting information.
    - Clear, actionable insights or recommendations if appropriate.
- Clearly cite all sources and provide links where possible.

Always be thorough, objective, and transparent in your methodology. If information is limited or uncertain, state this clearly and suggest next steps for further research.
"""


agent = Agent(
    name="Research Agent",
    description="An agent that can help you with your research using the internet.",
    system_prompt=RESEARCH_AGENT_SYSTEM_PROMPT,
    model=OpenAIModel(
        model_id="gpt-5",
    ),
    tools=[think, browser, batch],
    callback_handler=PrintingCallbackHandler(),
)


def main():
    print("🤖 Research Agent")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.")
    print("-" * 75)

    while True:
        try:
            user_input = input("\n> ").strip()
            if user_input.lower() in ["quit", "exit", "bye", "q"]:
                print("\n👋 Goodbye! Thanks for chatting with the Research Agent.")
                break
            if not user_input:
                continue
            _ = agent(user_input)
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for chatting with the Research Agent.")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or type 'quit' to exit.")


if __name__ == "__main__":
    main()
