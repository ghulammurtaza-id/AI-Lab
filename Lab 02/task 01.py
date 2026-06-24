class SecurityAgent:
    def __init__(self,agent_id,name,status):
        self.agent_id = agent_id
        self.name = name
        self.status = status

class FirewallAgent(SecurityAgent):
    def __init__(self,agent_id,name,status,traffic):
        self.traffic = traffic
        super().__init__(agent_id,name,status)
    def monitor_traffic(self):
        if(self.status):
            print(f"Currently {self.name} is monitoring {self.traffic} Traffics Nearly")
        else:
            print("Sorry he is sleeping")

class MalwareDetectionAgent(SecurityAgent):
    def __init__(self,agent_id,name,status,file):
        self.file = file
        super().__init__(agent_id,name,status)
    def scan_file(self):
        if(self.status):
            print(f"Currently {self.name} is scanning file {self.file}")
        else:
            print("Sorry he is sleeping")      
class AutomationAgent(SecurityAgent):
    def __init__(self,agent_id,name,status,routine_task):
        self.routine_task = routine_task
        super().__init__(agent_id,name,status)
    def run_automation(self):
        if(self.status):
            print(f"Currently {self.name} is Automating Task {self.routine_task}")
        else:
            print("Sorry he is sleeping")

a1 = FirewallAgent(1,"Rehman",True,23)
a2 = MalwareDetectionAgent(2,"Taaha",True,"home/security/bankfiles")
a3 = AutomationAgent(3,"Murtaza",True,"VibeCoding")     
a1.monitor_traffic()
a2.scan_file()
a3.run_automation()        