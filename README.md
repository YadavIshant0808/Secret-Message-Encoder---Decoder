# Secret Message Encoder & Decoder

## Overview

The **Secret Message Encoder & Decoder** is a simple Python program that allows you to convert your messages into a secret code and decode them back to their original form. The program applies a basic encoding algorithm that rearranges and augments the original message, making it difficult to understand without decoding.

## Features

- **Encoding**: Converts your message into a coded format by rearranging the letters and adding random characters as a prefix and suffix.
- **Decoding**: Reverts the coded message back to its original form.
- **Handles Short Words**: Words with less than three characters are simply reversed during encoding and decoded in the same way.

## How It Works

### Encoding

1. **Word Rearrangement**: For words with three or more characters, the first letter is moved to the end of the word.
2. **Random Characters**: A random 4-character prefix and suffix are added to each word.
3. **Short Words**: Words with fewer than three characters are simply reversed.

### Decoding

1. **Remove Random Characters**: The 4-character prefix and suffix are stripped from each word.
2. **Word Rearrangement**: The last letter of the remaining word is moved back to the front.
3. **Short Words**: Words with fewer than three characters are reversed back to their original form.

## How to Use

1. **Run the Program**: Start the program in a Python environment.
2. **Choose an Option**:
   - Press **'a'** to encode a message.
   - Press **'b'** to decode a message.
3. **Enter Your Message**: 
   - If encoding, input the message you want to convert into secret code.
   - If decoding, input the coded message you want to revert back to plain text.
4. **View the Result**: The program will output the encoded or decoded message based on your selection.

## Example Usage

### Encoding
```
Enter what you want to do:
 a. coding 
 b. Decoding 
a
Enter The word to code :
hello world
```

**Output**:
```
wXyZellohabcd YXvwolrdeFgh
```

### Decoding
```
Enter what you want to do:
 a. coding 
 b. Decoding 
b
Enter the Word to Decode :
wXyZellohabcd YXvwolrdeFgh
```

**Output**:
```
hello world
```

## Prerequisites

- Python 3.x installed on your machine.

## Installation

Simply download or copy the Python script to your local machine. No additional packages are required.

## License

This program is provided "as is" without any warranties. Feel free to modify and use it for your personal or educational projects.

# Author
Made by Ishant 
  with ❤️ in
     India