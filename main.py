from src.emails import EMAILS
from src.graphs.extraction import NOTICE_EXTRACTION_GRAPH


def main():

    for n, email in enumerate(EMAILS):
        print(f"Analyzing message {n + 1}")
        initial_state = {
            "notice_message": email,
            "notice_email_extract": None,
            "escalation_text_criteria": """There's a risk of fire or water damage at the site""",
            "escalation_dollar_criteria": 100_000,
            "requires_escalation": False,
            "escalation_emails": ["brog@abc.com", "bigceo@company.com"],
        }

        final_state = NOTICE_EXTRACTION_GRAPH.invoke(initial_state)
        print(final_state)


if __name__ == "__main__":
    main()
