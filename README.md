A template tool that processes the variable input directly from the filesystem.

Inspiration
===========

From time to time, we always have the need to run template for all developers. 
However, having to install dependency such as mustache executable has been annoying.

This is why we think a tool packaged as a docker image is useful. Inputs can be passed
in via docker volume parameters or environment variables. And those who need to run it 
can just run the docker image without having to install any executable.

The docker image is published as: `sohoffice/tempalte-tools`

Template variables
==================

General speaking the variables you can used come from the files inside the vars folder.
With the addition of `env` to access the environment variables.

The variables can be crossed referenced, but keep in mind they will be enhanced in the 
order of variable name, alphabetically ascending. This means the below might not have
the desired results, since VAR9 wasn't enhanced when VAR1 is being enhanced.

#### Bad example

```
VAR1 = `{{ VAR9 }}`
VAR9 = `{{ env["FOO"] }}`
```

Carefully design the template variable names so that the enhancement works in the right 
order.

#### Good example

```
VAR1 = `{{ env["FOO"] }}`
VAR2 = `{{ VAR1 }}`
```

Running with docker
===================

```
docker run -it --rm \
    -v "$PWD/sample/main.tmpl:/app/main.tmpl" \
    -v "$PWD/sample/vars:/app/vars" \
    --env "FOO=foo" \
    sohoffice/tempalte-tools:latest
```

Docker volumes
==============

| Path           | Description                                    |
|----------------|------------------------------------------------|
| /app/main.tmpl | The main template file. Must be a Jinja2 file. |
| /app/vars      | The directory to contain all variables.        |

Command line Usage
==================

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

References
==========

- [Github project](https://github.com/sohoffice/sohoffice-template-tools)
