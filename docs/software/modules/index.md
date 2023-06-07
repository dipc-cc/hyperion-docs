# Environment Modules

Environment modules provides a mechanism to dynamically modify a user's environment using modulefiles. A **modulefile** is a recipe required to load a particular application that may include setting environment variables; setting variables such as `PATH`, `LD_LIBRARY_PATH`, and `MANPATH` to include the location where an application is installed; loading dependent modules; and providing a brief description of the software.

## Module Commands

General usage: 
```
module [switches] [subcommand] [subcommand-args]
```

Further reading:

- `module --help`
- `man module`
- `man modulefile`
- [Environment Modules Documentation](https://modules.readthedocs.io/en/latest/) (note: some features may only be available in later versions than what is installed on NERSC systems)

## Command Summary
| Command                                   | Description                                               |

| ------------------------------------------| ----------------------------------------------------------|

| `module list`                             | List active modules in the user environment               |

| `module av[ail] [module]`                 | List available modules in MODULEPATH                      |

| `module add|load [module]`                | Load a module file in the user environment                |

| `module rm|unload [module]`               | Remove a *loaded* module from the user environment        |

| `module purge`                            | Remove all modules from the user environment              |

| `module swap|switch [module1] [module2]`  | Replace `module1` with `module2`                          |

| `module show|display [module]`            | Show content of commands performed by loading module file |

| `module help [module]`                    | Show help for a given module                              |

| `module whatis [module]`                  | A brief description of the module, generally single line  |

| `module use [-a] [path]`                  | Prepend or Append path to MODULEPATH                      |

| `module unuse [path]`                     | Remove path from MODULEPATH                               |

| `module keyword [text]`                   | Search for keyword across all module files                |


## Module Usage

Show availability of all modules containing a substring:

```shell

module avail -S <substring>
```

Loading a module to your current environment:

```shell
module load <module-name>
```

!!! tip

    If you load the name of a module (with no version), you will

    get the default version.

    ```shell
    module load Python
    ```

    To load a specific version use the full name:

    ```shell
    module load Python/3.10.4-GCCcore-11.3.0
    ```

To see all the loaded module:

```shell
module list
```

Remove a module from the current environment:

```shell
module unload <module-name>
```

To purge/remove all modules:

```shell
module purge
```


