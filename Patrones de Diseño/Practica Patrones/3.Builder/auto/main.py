from auto_director import AutoDirector
from fiat_builder import FiatBuilder
from ford_builder import FordBuilder

def main():
    auto_director = AutoDirector()

    # Crear un auto con Fiat
    fiat_builder = FiatBuilder()
    auto_director.set_auto_builder(fiat_builder)
    auto_director.build()
    print(auto_director.get_auto())

    # Crear un auto con Ford
    ford_builder = FordBuilder()
    auto_director.set_auto_builder(ford_builder)
    auto_director.build()
    print(auto_director.get_auto())

if __name__ == "__main__":
    main()