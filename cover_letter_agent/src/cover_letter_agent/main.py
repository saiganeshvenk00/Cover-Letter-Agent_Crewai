#!/usr/bin/env python


import os
from dotenv import load_dotenv

load_dotenv()

from cover_letter_agent.crew import CoverLetterCrew

os.makedirs('output', exist_ok=True)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'company': 'NVIDIA',
        'role': 'Product Manager'
    }


    result = CoverLetterCrew().crew().kickoff(inputs=inputs)

    print("Final cover letter: \n\n", result.raw)
    print("Cover letter saved to output/cover_letter.md")

if __name__ == "__main__":
    run()