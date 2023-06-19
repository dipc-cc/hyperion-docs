import mkdocs_gen_files


with mkdocs_gen_files.open("test.md", "w") as f:
    print("Hello, world!", file=f)
    print(" ", file=f)
    print("Hello, world! 2.0", file=f)
