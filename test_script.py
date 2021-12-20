import ezomero
import argparse

def main(msg):
    print("this is a test")
    conn = ezomero.connect()
    print(conn)
    print(msg)
    ezomero.print_groups(conn)
    conn.close()


if __name__ == "__main__":
    description = 'testing omero script and passing args'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('msg',
                        type=str,
                        help='message to be printed')
    args = parser.parse_args()

    main(args.msg)