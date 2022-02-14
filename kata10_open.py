def main():
    try:
        configuration = open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Could not find the config.txt file.")
        elif err.errno == 13:
            print("Found config file but could not read it.")
    except IsADirectoryError as err:
        print("Found config.txt but it is a directory, coyuld not read it: ", err)
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, cant complete reading configuration file!")
        

if __name__ == '__main__':
    main()