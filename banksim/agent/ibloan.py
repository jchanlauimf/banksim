from mesa import Agent


class Ibloan(Agent):
    ib_rate = None  # interbank loan rate
    ib_amount = None  # intferbank amount
    ib_last_color = None  # used to create visual effects
    ib_creditor = None
    ib_debtor = None

    def __init__(self, unique_id, model,libor_rate=0.01):
        super().__init__(unique_id, model)
        self.ib_rate = libor_rate
        self.ib_amount = 0