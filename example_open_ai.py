#!/usr/bin/env python3

"""
An openai api key is required to use this script.
This uses an advanced GPT-3 model and I also used AI via Github Copilot to write this command-line interface.
"""

import openai
import os
import click
from build_question_answer import submit_question


OPENAI_API_KEY = "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"


def submit_question(text):
    """This submits a question to OpenAI and returns the answer."""

    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = text

    result = openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model="text-davinci-002",
    )["choices"][0]["text"].strip("\n")
    return result


@click.command()
@click.argument("text")
def main(text):
    """This is the main function that you ask the OpenAI API a question to get an answer

    example: python3 example_open_ai.py "What is the meaning of life?"

    """

    print(submit_question(text))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
