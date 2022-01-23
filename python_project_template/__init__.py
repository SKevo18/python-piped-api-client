from typing import Generator
from random import random as rand



def infinitum(multiplier: int = 314) -> Generator[int, None, None]:
    """
        Generates an infinite sequence of random numbers.
    """
        
    while True:
        yield round(((rand() + 1) ** multiplier) % 21768543)



if __name__ == "__main__":
    count = 0
    max_count = 10

    for random in infinitum():
        print(random)
        count += 1

        if count >= max_count:
            break
