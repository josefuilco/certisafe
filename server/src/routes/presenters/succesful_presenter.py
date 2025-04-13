from dataclasses import dataclass

@dataclass
class SuccessfulPresenter:
    message: str
    success: bool = True