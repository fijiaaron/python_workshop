def say(first, *args, **kwargs):
	print(first)

	for arg in args:
		print(arg.capitalize())

	for (key, value) in kwargs.items():
		print(key + " = " +  value)

config = { "foo" : "bar", "bar" : "baz"}
say("ni", "ni", "nu", "none", x="y", **config)

