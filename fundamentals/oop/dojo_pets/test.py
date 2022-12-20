from classes.ninja import Ninja
from classes.pet import Pet
from classes.cat import Cat

naruto = Ninja(
    "Naruto", "Uzumaki", "biscuits", "pedigree", Cat("Puss in boots", "Disappear")
)

naruto.feed().walk().bathe()
