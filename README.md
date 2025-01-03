# YouTube Channel Availability Checker

This Python script helps you determine the availability of YouTube channel usernames. It reads a list of usernames from a text file, checks their availability on YouTube, and outputs the results.

## Features

- **Batch Checking**: Reads multiple channel names from a file (`list.txt`).
- **HTTP Request Handling**: Uses `requests` to interact with YouTube.
- **Output Results**: Saves unavailable channel names to `available_channels.txt`.
- **Error Handling**: Includes exceptions for common issues like missing input files.

## Requirements

- Python 3.x
- Required Libraries: `requests`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/riyadmondol2006/YouTube-Channel-Availability-Checker.git
   cd youtube-channel-checker
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

## Usage

1. Prepare a file named `list.txt` with one YouTube channel name per line (e.g., `youtube.com/@examplechannel`).
2. Run the script:
   ```bash
   python run.py
   ```
3. Check the output in `available_channels.txt` for usernames that are available.

## File Structure

- `run.py`: Main script.
- `list.txt`: Input file containing channel names to check.
- `available_channels.txt`: Output file with available channel names.

## Notes

- The script adds a delay between checks to avoid rate-limiting issues with YouTube.
- It uses a User-Agent header to mimic browser requests.

## Example

Input (`list.txt`):
```
name1
name2
name3
```

Output (`available_channels.txt`):
```
examplechannel
```

## Contributing

Feel free to fork the repository and submit pull requests for improvements.
