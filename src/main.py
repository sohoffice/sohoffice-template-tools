import logging
import os
from typing import List, Any

import click
from jinja2 import Environment, DictLoader

logging.basicConfig()
logger = logging.getLogger("sohoffice-template-tools")
logger.setLevel(logging.ERROR)


@click.command()
@click.argument('tmpl_file', type=click.File("r"))
@click.argument('var_dir', type=click.Path(exists=True))
@click.option('--format-type', type=click.Choice(['DEFAULT'], case_sensitive=False), default='DEFAULT',
              help="How to format the content. DEFAULT will trim the file content and add a newline in the end. "
                   "For directory, the file content will trimmed and add a newline before concatenated together.")
def main(tmpl_file, var_dir, format_type):
    """
    Process a Jinja2 template defined in TMPL_FILE and combined with context variables found in VAR_DIR to produce the output.

    TMPL_FILE must be a Jinja2 template file

    VAR_DIR is a directory where all elements are used as context variables. Simple file 'A' will be loaded as context variable 'A' and the
    file content as the value. Subdirectory 'B' will be loaded as context variable 'B' with all file content concatenated as the value.
    """
    logger.info(f"Template file: {tmpl_file}, variable directory: {var_dir}")
    main_content = tmpl_file.read()
    the_vars = {}
    formatter = select_formatter(format_type)
    for p in os.listdir(var_dir):
        a_path = os.path.join(var_dir, p)
        if os.path.isdir(a_path):
            the_vars[p] = formatter(read_dir(a_path))
        else:
            the_vars[p] = formatter(read_file(a_path))
    # Collect all variables and maintemplate into the_templates
    the_templates = the_vars.copy()
    the_templates['$main'] = main_content
    env = Environment(loader=DictLoader(the_templates))
    # Enhance the variables with environment variables
    the_vars['env'] = os.environ
    the_vars_keys = list(the_vars.keys())
    the_vars_keys.sort()
    for k in the_vars_keys:
        if k == 'env':
            continue
        var_tmpl = env.get_template(k)
        the_vars[k] = var_tmpl.render(the_vars)
    # Render the main template
    logger.debug(f"The variables: {the_vars}")
    main_tmpl = env.get_template('$main')
    print(main_tmpl.render(the_vars))


def read_file(p) -> str:
    with open(p) as f:
        return f.read()


def read_dir(d) -> List[str]:
    contents = []
    files = os.listdir(d)
    files.sort()
    for p in files:
        a_path = os.path.join(d, p)
        if os.path.isfile(a_path):
            contents.append(read_file(a_path))
    return contents


def select_formatter(format_type):
    if format_type == 'DEFAULT':
        return format_default


def format_default(some_input: Any) -> str:
    """
    Default format will trim the input and add a newline in the end of each line.
    """
    if type(some_input) == list:
        return '\n'.join([x.strip() for x in some_input])
    return some_input.strip() + '\n'


if __name__ == "__main__":
    main()
