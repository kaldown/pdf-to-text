## Usage:
1) Create `.envrc` file with `export OPENAI_API_KEY={OPENAI_API_KEY}`
2) Copy all the _pdf_ content into `text.py#BIGTEXT` constant
3) Create `artifacts/{NUMBER}` directory
4) Set `main#EXERCISE_NUMBER` equal to `{NUMBER}`
5) Run `main.py`
6) Run `./merger.sh artifacts/{NUMBER} {output}`

### Now you have `artifacts/{NUMBER}/{output}.mp3` file
