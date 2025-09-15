#!/usr/bin/env python3
"""
Entry point for Blueberry LLM inference.
This script redirects to the core inference functionality.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the main inference script
if __name__ == "__main__":
    from core.inference import main
    main()
