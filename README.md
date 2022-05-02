A template tool that processes the variable input directly from the filesystem.

Inspiration
===========

From time to time, we always have the need to run template for all developers. 
However, having to install dependency such as mustache executable has been annoying.

This tool is a perfect fit when packaged as a docker image. Inputs can be passed
in via docker volume parameters. And those who need to run this doesn't have to 
have any executable installed.

Published as docker image: `sohoffice/tempalte-tools`

Running example
===============

With docker

```
docker run -it --rm \
    -v "$PWD/sample/main.tmpl:/app/main.tmpl" \
    -v "$PWD/sample/vars:/app/vars" \
    sohoffice/tempalte-tools:latest
```

Docker volumes
==============

| Path           | Description                                    |
|----------------|------------------------------------------------|
| /app/main.tmpl | The main template file. Must be a Jinja2 file. |
| /app/vars      | The directory to contain all variables.        |

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
