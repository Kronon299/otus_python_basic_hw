from dataclasses import dataclass


@dataclass(frozen=True)
class Engine:
    """Class for engines."""
    type: str = 'diesel'
    max_speed: int = 100
    consumption_index: float = 1

    def real_speed(self,  max_cargo: float, cargo=0) -> float:
        if cargo == 0:
            return self.max_speed
        return self.max_speed * (0.5 * (cargo / max_cargo))


base_engine = Engine()
sport_engine = Engine(max_speed=250, consumption_index=1.5)


@dataclass(frozen=True)
class Horn:
    """Class for horns"""
    name: str = 'base horn'
    sound: str = 'Beep!'


base_horn = Horn()
loud_horn = Horn(name='Loud horn', sound='BEEEP!!')


if __name__ == '__main__':
    print(base_engine)
    print(sport_engine)
