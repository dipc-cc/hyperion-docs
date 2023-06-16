import mkdocs_gen_files


with mkdocs_gen_files.open("test.md", "w") as f:
    print("Hello, world!", file=f)
