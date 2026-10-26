from src.emails import EMAILS
from src.graphs.email_agent import email_agent_graph


def main():

    for n, email in enumerate(EMAILS):
        print(f"=> Analyzing message {n + 1}")

        escalation_criteria = (
            """There's an immediate risk of electrical, water, or fire damage"""
        )
        message_with_criteria = f"""
            The escalation criteria is: {escalation_criteria}
            
            Here's the email:
            
            {email}
        """

        message = {"messages": [("human", message_with_criteria)]}

        for chunk in email_agent_graph.stream(message, stream_mode="values"):
            chunk["messages"][-1].pretty_print()


if __name__ == "__main__":
    main()
