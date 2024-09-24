import argparse
from core.engine import Engine

def main():
    parser = argparse.ArgumentParser(description="Run the music visualizer")
    parser.add_argument("--mode", help="Specify a visualization mode")
    args = parser.parse_args()

    engine = Engine()
    if args.mode:
        if args.mode in engine.vis_manager.visualizations:
            engine.vis_manager.current_index = list(engine.vis_manager.visualizations.keys()).index(args.mode)
        else:
            print(f"Error: '{args.mode}' is not a valid visualization mode.")
            print("Available modes:", ", ".join(engine.vis_manager.visualizations.keys()))
            return

    engine.run()

if __name__ == "__main__":
    main()