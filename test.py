from pokemon_creator import *
import pytest
def test_creator():
    pid_caught_pokemon_dict_initializer()


    caught_pokemon_dict = create_pokemon('bulbasaur', 5, 0, {})
    assert caught_pokemon_dict[1].name == 'Bulbasaur'
    assert caught_pokemon_dict[1].types == ['grass', 'poison']
    # assert caught_pokemon_dict[1].moves.keys() == ['Tackle', 'Growl']

    caught_pokemon_dict = create_pokemon('mew', 10, 1, caught_pokemon_dict)
    assert caught_pokemon_dict[2].species == 'Mew'
    assert caught_pokemon_dict[2].types == ['psychic']
    # assert caught_pokemon_dict[2].moves.keys() == ['Pound', 'Transform']


    for move in poke_move_dict:
        move_keys = []
        for key in poke_move_dict[move]:
            move_keys.append(key)
        assert move_keys == ['Effect', 'Type', 'PP', 'Power', 'Accuracy', 'Category']


from pokemon_dict import *
def test_pokemon_dict():
    assert pokemon_dict['Pikachu']['types'] == ['electric']

from poke_move_dict import *
def test_move_dict():
    assert poke_move_dict['Thunder']['Power'] == 110



pytest.main(["-v", "--tb=line", "-rN", __file__])