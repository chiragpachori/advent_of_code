# --- Day 5: Supply Stacks ---

[Question Link](https://adventofcode.com/2022/day/5) | [Reddit Solution Thread](https://www.reddit.com/r/adventofcode/comments/zcxid5/2022_day_5_solutions/)

## Goals:

- [ ] Zero import
- [x] Within 24 hours
- [ ] ~ Did a one line solution

## Thoughts:

1. Parsing the crate stack was a bit tricky, but I am happy with this approach of using list of lists
2. Can't really think of a one line approach to it, although it can be condensed a bit using 2 levels of list 
comprehension while creating the block list
3. Doing it without imports is possible if I replace the ascii uppercase set from string module by writing A-Z
4. Using parse (module) seems like a good idea here, but I need to brush up some regex skills
