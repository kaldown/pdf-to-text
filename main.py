from pathlib import Path
from openai import OpenAI

from split import split_text_into_blocks
from text import BIGTEXT

_VOICES = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

EXERCISE_NUMBER = 6
FOLDER_ROOT = Path(__file__).parent / "artifacts" / f"{EXERCISE_NUMBER}"

if __name__ == "__main__":
    client = OpenAI()

    for i, text in enumerate(split_text_into_blocks(BIGTEXT)):
        speech_file_path = FOLDER_ROOT / f"{i}.mp3"

        voice = _VOICES[i % len(_VOICES)]

        with client.audio.speech.with_streaming_response.create(
          model="tts-1",
          voice=voice,
          input=text,
        ) as response:
          response.stream_to_file(speech_file_path)
