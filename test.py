import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <arg1> <arg2> ...")
        sys.exit(1)
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
if __name__ == "__main__":
    main()