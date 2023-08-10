FILE_STRUCTURE = [
    "title-short",
    "title-long",
    "date",
    "date-human",
    "quote",
    "attribution",
    "content",
]


def generate(filepath, write_to_file=True):
    """
    Takes an input file and returns a html file fitting the style of the blog.
    """
    replacements_dict = _create_replacements_dict(filepath)
    populated_template = _populate_template(replacements_dict)

    if write_to_file:
        with open(f"{replacements_dict['title-short'].lower().replace(' ', '_')}.html", "w") as f:
            f.write(populated_template)
    return populated_template


def _create_replacements_dict(filepath):
    """
    Takes the filepath of the markdown document as an argument.

    Returns a dictionary of all of the replacements we want to make.
    """
    replacements_dict = {}
    with open(filepath, "r") as f:
        ls = f.readlines()
        for l in ls:
            k = FILE_STRUCTURE.pop(0)

            if k == "content":
                i = ls.index(l)
                v = (''.join(ls[i:])).replace(f"{k}:", "").strip()
                # I know this is a bit of a crappy solution, but I have spent too
                # much time on this while I should have been studying!
                replacements_dict[k] = v
                break
            else:
                v = l.replace(f"{k}:", "").strip()
                replacements_dict[k] = v

    return replacements_dict


def _populate_template(replacements_dict):
    """
    Takes a dictionary of replacements as an argument, and uses these values to populate the template.
    """
    with open("./templates/blog_post.html", "r") as f:
        template = f.read()

    for k, v in replacements_dict.items():
        template = template.replace(f"{{% {k} %}}", v)

    return template
