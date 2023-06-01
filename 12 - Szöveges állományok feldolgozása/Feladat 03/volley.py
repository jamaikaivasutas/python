class Volley:
    def __init__(self):
        super().__init__()
        self.playerName: str = None
        self.playerHeight: int = 0
        self.playerPost: str = None
        self.playerNationality: str = None
        self.playerTeam: str = None
        self.playerCountry: str = None

    def __str__(self) -> str:
        return f"{self.playerName} {self.playerHeight} {self.playerPost} {self.playerNationality} {self.playerTeam} {self.playerCountry}"

        