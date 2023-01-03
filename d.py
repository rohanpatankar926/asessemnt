def main():
    import argparse
    parse=argparse.ArgumentParser()
    parse.add_argument("--param1",type=int,default=1,required=True)
    parse.add_argument("--param2",type=int,default=1000,required=True)
    parser=parse.parse_args()
    print(parser.param1)
    return parser
main()