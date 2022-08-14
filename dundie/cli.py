import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Dunder Miffline Rewards CLI",
        epilog="Enjoy and use with cautious.",    
    )
    
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
        default="help",
    )
    
    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
    )
    
    args = parser.parse_args()
    globals()[args.subcommand](args.filepath)