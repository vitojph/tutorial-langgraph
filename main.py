from src.chains.extraction import NOTICE_PARSER_CHAIN
from src.emails import EMAILS


def main():

    for n, email in enumerate(EMAILS):
        print(f"Analyzing message {n + 1}")
        res = NOTICE_PARSER_CHAIN.invoke({"message": email})
        print(res.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
