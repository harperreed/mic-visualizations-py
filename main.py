import argparse
from dotenv import load_dotenv
from core.engine import Engine
import asyncio

async def main():
    load_dotenv()

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

    await engine.vis_manager.start()
    await engine.run()

if __name__ == "__main__":
    asyncio.run(main())