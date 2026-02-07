class Threat:
    def __init__(self, threatid, name, severity):
        self.threat_id = threatid
        self.name = name
        self.severity = severity


class Phishing(Threat):
    def __init__(self, threatid, name, severity, emails):
        super().__init__(threatid, name, severity)
        self.emails = emails

    def analyzemail(self):
        print(f"{self.name} is analyzing emails: {self.emails}")


class Ransomware(Threat):
    def __init__(self, threatid, name, severity, monitorfile):
        super().__init__(threatid, name, severity)
        self.file = monitorfile

    def scan_files(self):
        print(f"{self.name} is scanning files: {self.file}")


class Botnet(Threat):
    def __init__(self, threatid, name, severity, networktraffic):
        super().__init__(threatid, name, severity)
        self.traffic = networktraffic

    def detecttraffic(self):
        print(f"{self.name} is detecting network traffic: {self.traffic}")


def main():
    p1 = Phishing(101, "Phishing Attack", "High", ["mail1@gmail.com", "mail2@gmail.com"])
    r1 = Ransomware(102, "Ransomware Attack", "Critical", ["file1.exe", "file2.doc"])
    b1 = Botnet(103, "Botnet Attack", "Medium", "Suspicious Network Packets")


    p1.analyzemail()
    r1.scan_files()
    b1.detecttraffic()


if __name__ == "__main__":
    main()
