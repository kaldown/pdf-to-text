import asyncio
from pathlib import Path
from openai import AsyncOpenAI

from split import split_text_into_blocks
from text import BIGTEXT

_VOICES = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

EXERCISE_NUMBER = 6
FOLDER_ROOT = Path(__file__).parent / "artifacts" / f"{EXERCISE_NUMBER}"


async def fetch_file(speech_file_path: Path, text: str, voice: str, client: AsyncOpenAI) -> None:
    async with client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice=voice,
            input=text,
    ) as response:
        await response.stream_to_file(speech_file_path)


async def main():
    client = AsyncOpenAI()
    tasks = []

    for i, text in enumerate(split_text_into_blocks(BIGTEXT)):
        speech_file_path = FOLDER_ROOT / f"{i}.mp3"
        voice = _VOICES[i % len(_VOICES)]
        tasks.append(fetch_file(speech_file_path=speech_file_path, text=text, voice=voice, client=client))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
