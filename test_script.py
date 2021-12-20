import ezomero
import argparse
import ast
from omero.clients import BaseClient
from omero.gateway import BlitzGateway

def main(id, kv):
    print("this is a test")
    print(id)
    print(kv)
    params = ast.literal_eval(kv)
    print(params)
    data_type = params['Data_Type']
    data_id = params['IDs']
    ann = {params['Key']:params['Value'][0]}
    client = BaseClient(host='ctomerodev.jax.org')
    client.joinSession(id)
    conn = BlitzGateway(client_obj=client)
    ezomero.print_groups(conn)
    ezomero.post_map_annotation(conn, data_type, data_id, ann, ns='test')
    conn.close()


if __name__ == "__main__":
    description = 'testing omero script and passing args'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('id',
                        type=str,
                        help='uuid of the session to be used')
    parser.add_argument('kv',
                        type=str,
                        help='dictionary with kv pair and where to put it')
    args = parser.parse_args()

    main(args.id, args.kv)