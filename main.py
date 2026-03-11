from supervisor_agent import SupervisorAgent


def main():

    supervisor = SupervisorAgent()

    print("Multi-Agent System Started")
    print("Type 'exit' to stop\n")

    while True:

        query = input("User: ")

        if query.lower() == "exit":
            break

        result = supervisor.route(query)

        print("\nAgent:", result, "\n")


if __name__ == "__main__":
    main()