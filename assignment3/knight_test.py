def test_knights():
	knight = "Bedevere"
	print("knight is : " + knight)
	assert knight == "Bedevere"

def test_knights_who_say_ni():
	knight = "Galahad"
	print(knight + " says " + say(knight))
	assert say(knight) == "Ni"

def say(knight):
	if knight == "Bedevere":
		return("Nu")
	else:
		return("Ni")
