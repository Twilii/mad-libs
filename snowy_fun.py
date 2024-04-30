# Words the player needs to provide
adjective1 = input("Enter an adjective: ").lower()
game = input("Enter the name of an outdoor game: ").lower()
adjective2 = input("Enter another adjective: ").lower()
friend = input("Enter the name of a friend (or any name if you're friendless): ").capitalize()
verb = input("Enter a verb ending in 'ing': ").lower()
adjective3 = input("Enter one more adjective: ").lower()

# Story template
story = (f"""It was a(n) {adjective1} winter day at the ski resort. My friends and I were in the snow playing {game}. As a(n) {adjective2} bear approached, my friend,
{friend}, yelled, "Look! There\'s a bear {verb}!" As we got closer, we saw that the bear was indeed {verb}! {friend} ran away and into the lodge.
{friend} was afraid of the {verb} bear. The rest of us stayed in the snow playing {game} because {verb} bears are {adjective3}.""")

# Print story
print(story)
