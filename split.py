def split_text_into_blocks(text: str, max_length=4000) -> list[str]:
    if not text or not text.strip():
        raise ValueError

    blocks = []
    current_block = ""

    for sentence in text.split('. '):
        sentence += '. '
        if len(current_block) + len(sentence) <= max_length:
            current_block += sentence
        else:
            blocks.append(current_block.strip())
            current_block = sentence

    if current_block:
        blocks.append(current_block.strip())

    return blocks
