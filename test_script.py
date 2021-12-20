import ezomero
import argparse
from omero.clients import BaseClient
from omero.gateway import BlitzGateway

def main(id):
    print("this is a test")
    print(id)
    client = BaseClient()
    client.joinSession(id)
    conn = BlitzGateway(client_obj=client)
    ezomero.print_groups(conn)
    conn.close()


if __name__ == "__main__":
    description = 'testing omero script and passing args'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('id',
                        type=str,
                        help='uuid of the session to be used')
    args = parser.parse_args()

    main(args.id)