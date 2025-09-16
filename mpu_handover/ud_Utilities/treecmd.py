# import os
# import argparse

# def list_files(startpath, show_hidden=False, max_depth=None):
#     for root, dirs, files in os.walk(startpath):
#         # Calculate the depth of the current directory
#         depth = root[len(startpath):].count(os.sep)
        
#         # Skip hidden files and directories if show_hidden is False
#         if not show_hidden:
#             dirs[:] = [d for d in dirs if not d.startswith('.')]
#             files = [f for f in files if not f.startswith('.')]
        
#         # If max_depth is specified and the current depth exceeds it, skip this directory
#         if max_depth is not None and depth >= max_depth:
#             dirs[:] = []
#             continue
        
#         indent = ' ' * 4 * (depth)
#         print(f"{indent}{os.path.basename(root)}/")
        
#         subindent = ' ' * 4 * (depth + 1)
#         for f in files:
#             print(f"{subindent}{f}")

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Python script to mimic the 'tree' command.")
#     parser.add_argument("directory", nargs="?", default=".", help="Directory to list (default: current directory)")
#     parser.add_argument("-a", "--all", action="store_true", help="Include hidden files and directories")
#     parser.add_argument("-L", "--level", type=int, help="Max display depth of the directory tree")

#     args = parser.parse_args()

#     list_files(args.directory, show_hidden=args.all, max_depth=args.level)










import os
import argparse

def list_files(startpath, show_hidden=False, max_depth=None, show_full_path=False):
    for root, dirs, files in os.walk(startpath):
        # Calculate the depth of the current directory
        depth = root[len(startpath):].count(os.sep)
        
        # Skip hidden files and directories if show_hidden is False
        if not show_hidden:
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files = [f for f in files if not f.startswith('.')]
        
        # If max_depth is specified and the current depth exceeds it, skip this directory
        if max_depth is not None and depth >= max_depth:
            dirs[:] = []
            continue
        
        indent = ' ' * 4 * (depth)
        if show_full_path:
            print(f"{indent}{root}/")
        else:
            print(f"{indent}{os.path.basename(root)}/")
        
        subindent = ' ' * 4 * (depth + 1)
        for f in files:
            if show_full_path:
                print(f"{subindent}{os.path.join(root, f)}")
            else:
                print(f"{subindent}{f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python script to mimic the 'tree' command.")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to list (default: current directory)")
    parser.add_argument("-a", "--all", action="store_true", help="Include hidden files and directories")
    parser.add_argument("-L", "--level", type=int, help="Max display depth of the directory tree")
    parser.add_argument("-f", "--full-path", action="store_true", help="Show full path of the listed files and directories")

    args = parser.parse_args()

    list_files(args.directory, show_hidden=args.all, max_depth=args.level, show_full_path=args.full_path)
