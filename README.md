# Text Summarization with FLAN-T5

## Overview

This Python script uses the FLAN-T5 model to preprocess a text file, generate a summary, and print the number of tokens before and after summarization. The script utilizes the `transformers` library from Hugging Face for model loading and tokenization.

## Features

- **Text Preprocessing**: Cleans the text by removing URLs and punctuation, and converting it to lowercase.
- **Text Summarization**: Uses the FLAN-T5 model to generate a summary of the input text.
- **Token Count Analysis**: Prints the number of tokens before and after summarization.

## Requirements

- Python 3.7+
- `transformers` library
- `torch` library
- Ensure you have the FLAN-T5 model available for download.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/text-summarization.git
    cd text-summarization
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install torch transformers
    ```

## Usage

1. **Save your text to a file** (e.g., `excel text.txt`) and place it in the appropriate directory.

2. **Update the `input_file_path`** in the script to point to the location of your text file:

    ```python
    input_file_path = r"C:\Users\MORNING SHIFT\Downloads\excel text.txt"
    ```

3. **Run the script**:

    ```bash
    python summarization_script.py
    ```

4. **Review the output**, which includes:
   - The generated summary.
   - The number of tokens before summarization.
   - The number of tokens after summarization.

## Script Details

- **`preprocess_text(text)`**: Function to clean the text by removing URLs and punctuation, and converting it to lowercase.
- **`input_file_path`**: Path to the text file to be summarized.
- **`model`**: Loads the FLAN-T5 model for text summarization.
- **`tokenizer`**: Tokenizes the text for the model input.
- **`input_tokens_before`**: Number of tokens in the preprocessed text.
- **`summary_ids`**: Generated summary from the model.
- **`summary_tokens`**: Number of tokens in the generated summary.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## Contact

For any questions or inquiries, please contact [njnagaraj007@gmail.com].


## Support the project

<a href="https://www.linkedin.com/in/nagarajanbj/" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-black.png" alt="Buy Me A Coffee" height="45" width="163" ></a>


#### Happy Coding  ♥️
