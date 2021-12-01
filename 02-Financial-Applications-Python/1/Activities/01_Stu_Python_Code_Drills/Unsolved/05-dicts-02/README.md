## Traversing Through Dictionaries

In this challenge, you are given a large dictionary `show_data.py`. Your job is to navigate through this dictionary and answer the prompts via key-value pairs.

Here's an example:

**Prompt:** What actor plays Ned Stark in _Game of Thrones_ (drama)?

**Correct Answer:**

`shows["genre"]["drama"]["game_of_thrones"]["cast"][0]["actor"]`

## Instructions

Open the [starter file](Unsolved/dicts-02.py) and perform the following:

1. Use the `from` keyword to import the `shows` dictionary from the `show_data.py` file.

2. Answer each question by printing the expected result using bracket notation for the `show` dictionary.

## Hint

In this activity, you may find that you're repeating yourself a lot. It may be helpful to create variables that point to different locations within the dictionary. For example:

`drama = shows["genre"]["drama"]`

Then, to get the actor who plays Rick in _The Walking Dead_, we would simply write:

`drama["the_walking_dead"]["cast"][0]["actor"]`

As opposed to:

`shows["genre"]["drama"]["the_walking_dead"]["cast"][0]["actor"]`.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
