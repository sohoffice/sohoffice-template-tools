A template tool that processes the variable input directly from the filesystem.

Inspiration
===========

This tool is a perfect fit when packaged as a docker image. Inputs can be passed
in via docker parameters. And those who need this doesn't have to have any executable
installed.

This will be published as docker image `sohoffice/tempalte-tools`

Running example
===============

With docker

```
docker run -it --rm \
    -v "$PWD/sample/main.tmpl:/app/main.tmpl" \
    -v "$PWD/sample/vars:/app/vars" \
    sohoffice/tempalte-tools:latest
```

Usage
=====

```
Usage: main.py [OPTIONS] TMPL_FILE VAR_DIR

  Process a Jinja2 template defined in TMPL_FILE and combined with context
  variables found in VAR_DIR to produce the output.

  TMPL_FILE must be a Jinja2 template file

  VAR_DIR is a directory where all elements are used as context variables.
  Simple file 'A' will be loaded as context variable 'A' and the file content
  as the value. Subdirectory 'B' will be loaded as context variable 'B' with
  all file content concatenated as the value.

Options:
  --format-type [DEFAULT]  How to format the content. DEFAULT will trim the
                           file content and add a newline in the end. For
                           directory, the file content will trimmed and add a
                           newline before concatenated together.
  --help                   Show this message and exit.

```
