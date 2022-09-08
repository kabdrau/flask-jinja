"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text):
        """Create story with words and template text."""

        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

story1 = Story(
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "An Excited Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

story3 = Story(
    "Old Macdonald",
    ["adjective", "noun", "animal", "noise"],
    """{adjective} Macdonald had a {noun}, E-I-E-I-O \n
    and on that {noun} he had an {animal}, E-I-E-I-O \n
    with a {noise} {noise} here \n 
    and a {noise} {noise} there, \n
    here a {noise}, there a {noise}, \n
    everywhere a {noise} {noise}, \n
    {adjective} Macdonald had a {noun}, E-I-E-I-O."""
)

# Make dict of {code:story, code:story, ...}
stories = {s.title: s for s in [story1, story2, story3]}