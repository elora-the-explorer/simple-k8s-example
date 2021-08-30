from simple_app import greet, greetings, unsupported_language_message

def test_greet_defaults_to_maori():
    assert greet() == greetings.get('maori')

def test_greet_can_select_different_language():
    assert greet('french') == greetings.get('french')

def test_greet_selects_correct_language_when_language_capitalised():
    assert greet('English') == greetings.get('english')

def test_greet_can_handle_unknown_language(): 
    assert greet('flibber') == unsupported_language_message


