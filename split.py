def split_text_into_blocks(text, max_length=4000):
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
