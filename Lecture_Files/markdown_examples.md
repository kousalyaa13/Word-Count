# Top level header: good for an overall title

## Level 2 header: good for a section

## Some basics

### Text styles

*Emphasized* text

**Bold** text

`code-style` text

### Simple lists

- Bullet 1
- Bullet 2
  - sub-bullet
- Bullet 3

Also ordered lists with numbering:

1. First thing
2. Second thing
   1. sublist
   2. more on the sublist
3. Third thing

## Here's some other nifty things

### Links

Here are some handy links:

- [Original Markdown page](https://daringfireball.net/projects/markdown/syntax)
- [Another good markdown reference page](https://www.markdownguide.org/)
- [Official VS Code page describing how VS Code works with Markdown](https://code.visualstudio.com/Docs/languages/markdown)


### Code blocks

Here's a block of code, for fancy display:

```python
# Use this:
with open(file_path, "r") as file_connection:
    file_contents = file_connection.read()

# NOT this:
file_connection = open(file_path, "r")
file_contents = file_connection.read()
file_connection.close()
```

### Tables



Note the colon on the right of the dashes ( ---: ) this makes that column align to the right.

| grade category | total points|
|--- | ---: |
| Fundamental Python Patterns | 64|
| Special Topic Patterns | 10 |
| Participation | 10 |
| Ethical Programming Practices | 8 |
| Tools & Interfaces | 8 |
| TOTAL | 100 |

### Images

And here's an image:

![a big step for comedy](./silly_walk.jpeg)

### Emoji

Copy & paste from [this very fine site](https://emojipedia.org/)

🎃

But also: :jack_o_lantern: (this only renders when you have the Markdown Emoji extension installed)

And here's a [page with a list of emoji shortcodes](https://gist.github.com/rxaviers/7360908)

# Make your documentation readable and fun!