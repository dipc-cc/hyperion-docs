import mkdocs_gen_files

with mkdocs_gen_files.open("test.txt", "w") as f:
    print("Hello, world!", file=f)
