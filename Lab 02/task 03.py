class agentgeneral:
    def execute_response(self):
        print("he do all general work ")
class AlertAgent(agentgeneral):
    def execute_response(self):
        print("Now send notification yeah ")

class BlockAgent(agentgeneral):
    def execute_response(self):
        print("this block the activities btw yep")

class RecoverAgent(agentgeneral):
    def execute_response(self):
        print("currently busy store affected system")
        
def main():
    a1 = agentgeneral()
    a2 = AlertAgent()
    a3 = BlockAgent()
    a4 = RecoverAgent()

    agents = [a1, a2, a3, a4]

    print("---- Agent Responses ----")
    for agent in agents:
        agent.execute_response()


if __name__ == "__main__":
    main()
